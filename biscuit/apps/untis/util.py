from datetime import date, time
from typing import BinaryIO, Optional, Union
from xml.dom import minidom, Node

from django.http import HttpRequest
from django.utils.translation import ugettext as _

from biscuit.apps.chronos.models import Subject, TimePeriod, Room, Lesson
from biscuit.core.models import Group, Person
from biscuit.core.util import messages


def get_child_node_text(node: Node, tag: str) -> Optional[str]:
    tag_nodes = node.getElementsByTagName(tag)

    if len(tag_nodes) == 1:
        return tag_nodes[0].firstChild.nodeValue
    else:
        return None


def get_child_node_id(node: Node, tag: str) -> Optional[str]:
    tag_nodes = node.getElementsByTagName(tag)

    if len(tag_nodes) == 1:
        return tag_nodes[0].attributes['id'].value
    else:
        return None


def untis_import_xml(request: HttpRequest, untis_xml: Union[BinaryIO, str]) -> None:
    dom = minidom.parse(untis_xml)

    subjects = dom.getElementsByTagName('subject')
    for subject_node in subjects:
        abbrev = subject_node.attributes['id'].value[3:]
        name = get_child_node_text(subject_node, 'longname')
        colour_fg = get_child_node_text(subject_node, 'forecolor')
        colour_bg = get_child_node_text(subject_node, 'backcolor')

        subject, created = Subject.objects.get_or_create(abbrev=abbrev, defaults={
            'name': name, 'colour_fg': colour_fg, 'colour_bg': colour_bg})

    periods = dom.getElementsByTagName('timeperiod')
    for period_node in periods:
        weekday = int(get_child_node_text(period_node, 'day'))
        period = int(get_child_node_text(period_node, 'period'))
        starttime = get_child_node_text(period_node, 'starttime')
        endtime = get_child_node_text(period_node, 'endtime')

        time_start = time(int(starttime[:2]), int(starttime[2:]))
        time_end = time(int(endtime[:2]), int(endtime[2:]))

        period, created = TimePeriod.objects.get_or_create(weekday=weekday, period=period, defaults={
            'time_start': time_start, 'time_end': time_end})

    rooms = dom.getElementsByTagName('room')
    for room_node in rooms:
        short_name = room_node.attributes['id'].value[3:]
        name = get_child_node_text(room_node, 'longname')

        room, created = Room.objects.get_or_create(short_name=short_name, defaults={
            'name': name})

    classes = dom.getElementsByTagName('class')
    for class_node in classes:
        short_name = class_node.attributes['id'].value[3:]
        name = _('Class %s') % short_name
        class_teacher_short_name = get_child_node_id(
            class_node, 'class_teacher')[3:]

        class_, created = Group.objects.get_or_create(short_name=short_name, defaults={
            'name': name})

        try:
            class_.owners.set([Person.objects.get(
                short_name=class_teacher_short_name)])
            class_.save()
        except Person.DoesNotExist:
            messages.warning(request, _('Could not set class teacher of %(class)s to %(teacher)s.') % {
                'class': short_name, 'teacher': class_teacher_short_name})

    Lesson.objects.all().delete()

    lessons = dom.getElementsByTagName('lesson')
    for lesson_node in lessons:
        subject_abbrev = get_child_node_id(lesson_node, 'lesson_subject')[3:]
        teacher_short_name = get_child_node_id(
            lesson_node, 'lesson_teacher')[3:]
        group_short_names = [v[3:] for v in get_child_node_id(
            lesson_node, 'lesson_classes').split(' ')]
        effectivebegindate = get_child_node_text(
            lesson_node, 'effectivebegindate')
        effectiveenddate = get_child_node_text(lesson_node, 'effectiveenddate')

        times = lesson_node.getElementsByTagName('time')
        time_periods = []
        for time_node in times:
            day = int(get_child_node_text(time_node, 'assigned_day'))
            period = int(get_child_node_text(time_node, 'assigned_period'))

            room_id = get_child_node_id(time_node, 'assigned_room')
            room = room_id[3:] if room_id else None

            time_periods.append((day, period, room))

        subject = Subject.objects.get(abbrev=subject_abbrev)
        periods = [(TimePeriod.objects.get(
            weekday=v[0], period=v[1]), Room.objects.get(short_name=v[2]) if v[2] else None) for v in time_periods]
        date_start = date(int(effectivebegindate[:4]), int(effectivebegindate[4:6]), int(
            effectivebegindate[6:])) if effectivebegindate else None
        date_end = date(int(effectiveenddate[:4]), int(effectiveenddate[4:6]), int(
            effectiveenddate[6:])) if effectiveenddate else None

        try:
            groups = [Group.objects.get(short_name=v)
                      for v in group_short_names]
        except Group.DoesNotExist:
            messages.error(request, _('Invalid list of classes: %s') %
                           ', '.join(group_short_names))
            continue

        try:
            teachers = [Person.objects.get(short_name=teacher_short_name)]
        except Person.DoesNotExist:
            messages.error(request, _(
                'Failed to import lesson: Teacher %s does not exist.') % teacher_short_name)
            continue

        lesson = Lesson.objects.create(
            subject=subject, date_start=date_start, date_end=date_end)

        lesson.groups.set(groups)
        lesson.teachers.set(teachers)

        for period in periods:
            lesson.periods.add(period[0], through_defaults={'room': period[1]})

        lesson.save()
