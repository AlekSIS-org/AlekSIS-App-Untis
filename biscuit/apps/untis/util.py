from datetime import date, time
from xml.dom import minidom

from biscuit.apps.cambro.models import Room
from biscuit.apps.chronos.models import Subject, TimePeriod, Lesson
from biscuit.core.models import Group, Person


def get_child_node_text(node, tag):
    tag_nodes = node.getElementsByTagName(tag)

    if len(tag_nodes) == 1:
        return tag_nodes[0].firstChild.nodeValue
    else:
        return None


def get_child_node_id(node, tag):
    tag_nodes = node.getElementsByTagName(tag)

    if len(tag_nodes) == 1:
        return tag_nodes[0].attributes['id'].value
    else:
        return None


def untis_import_xml(request, untis_xml):
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

    lessons = dom.getElementsByTagName('lesson')
    for lesson_node in lessons:
        subject_abbrev = get_child_node_id(lesson_node, 'lesson_subject')[3:]
        teacher_short_name = get_child_node_id(
            lesson_node, 'lesson_teacher')[3:]
        group_short_names = [v[:3] for v in get_child_node_id(
            lesson_node, 'lesson_classes').split(' ')]
        effectivebegindate = get_child_node_text(
            lesson_node, 'effectivebegindate')
        effectiveenddate = get_child_node_text(lesson_node, 'effectiveenddate')

        times = lesson_node.getElementsByTagName('time')
        time_periods = []
        for time_node in times:
            day = get_child_node_text(time_node, 'assigned_day')
            period = get_child_node_text(time_node, 'assigned_period')
            time_periods.append((day, period))

        subject = Subject.objects.get(abbrev=subject_abbrev)
        teachers = [Person.objects.get(short_name=teacher_short_name)]
        groups = [Group.objects.get(short_name=v) for v in group_short_names]
        periods = [TimePeriod.objects.get(
            weekday=v[0], period=v[1]) for v in time_periods]
        date_start = date(int(effectivebegindate[:4]), int(effectivebegindate[4:6]), int(
            effectivebegindate[6:])) if effectivebegindate else None
        date_end = date(int(effectiveenddate[:4]), int(effectiveenddate[4:6]), int(
            effectiveenddate[6:])) if effectiveenddate else None

        lesson, created = Lesson.objects.get_or_create(groups=groups, periods=periods, defaults={
                                                       'subject': subject, 'teachers': teachers, 'date_start': date_start, 'date_end': date_end})
