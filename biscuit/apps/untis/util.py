from datetime import time
from xml.dom import minidom

from biscuit.apps.cambro.models import Room
from biscuit.apps.chronos.models import Subject, TimePeriod
from biscuit.core.models import Group


def get_child_node_text(node, tag):
    tag_nodes = node.getElementsByTagName(tag)

    if len(tag_nodes) == 1:
        return tag_nodes[0].firstChild.nodeValue
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
