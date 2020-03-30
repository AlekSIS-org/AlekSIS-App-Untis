import logging
from datetime import time
from typing import List, Dict

from constance import config

from aleksis.apps.chronos import models as chronos_models
from aleksis.core import models as core_models

from .... import models as mysql_models
from ..util import run_default_filter, untis_colour_to_hex, untis_split_first

logger = logging.getLogger(__name__)


def import_subjects() -> Dict[int, chronos_models.Subject]:
    """ Import subjects """

    subjects_ref = {}

    # Get subjects
    subjects = run_default_filter(mysql_models.Subjects.objects, filter_term=False)

    for subject in subjects:
        # Check if needed data are provided
        if not subject.name:
            logger.error(
                "Subject ID {}: Cannot import subject without short name.".format(
                    subject.subject_id
                )
            )
            continue

        # Build values
        short_name = subject.name[:10]
        name = subject.longname[:30] if subject.longname else short_name
        colour_fg = untis_colour_to_hex(subject.forecolor)
        colour_bg = untis_colour_to_hex(subject.backcolor)
        import_ref = subject.subject_id

        # Get or create subject object by short name
        new_subject, created = chronos_models.Subject.objects.get_or_create(
            abbrev=short_name,
            defaults={
                "name": name,
                "colour_fg": colour_fg,
                "colour_bg": colour_bg,
                "import_ref_untis": import_ref,
            },
        )

        # Force sync
        if config.UNTIS_IMPORT_MYSQL_UPDATE_SUBJECTS and (
            new_subject.name != name
            or new_subject.colour_fg != colour_fg
            or new_subject.colour_bg != colour_bg
            or new_subject.import_ref_untis != import_ref
        ):
            new_subject.name = name
            new_subject.colour_fg = untis_colour_to_hex(subject.forecolor)
            new_subject.colour_bg = untis_colour_to_hex(subject.backcolor)
            new_subject.import_ref_untis = import_ref
            new_subject.save()

        logger.info("Successfully imported subject {} ({})".format(short_name, "created" if created else "updated"))

        subjects_ref[import_ref] = new_subject

    return subjects_ref


def import_teachers() -> Dict[int, core_models.Person]:
    """ Import teachers """

    teachers_ref = {}
    teachers = run_default_filter(mysql_models.Teacher.objects)
    for teacher in teachers:
        if not teacher.name:
            raise Exception("Short name needed.")

        short_name = teacher.name[:5]
        first_name = teacher.firstname if teacher.firstname else "?"
        last_name = teacher.longname if teacher.longname else teacher.name

        new_teacher, created = core_models.Person.objects.get_or_create(
            short_name__iexact=short_name,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "import_ref": teacher.teacher_id,
            },
        )

        new_teacher.short_name = short_name
        new_teacher.save()

        teachers_ref[teacher.teacher_id] = new_teacher

    return teachers_ref


def import_classes(
    teachers_ref: Dict[int, core_models.Person]
) -> Dict[int, core_models.Group]:
    """ Import classes """

    classes_ref = {}
    course_classes = run_default_filter(mysql_models.Class.objects, filter_term=True)

    for class_ in course_classes:
        if not class_.name:
            raise Exception("Short name needed.")

        short_name = class_.name[:16]
        name = class_.longname if class_.longname else short_name
        teacher_ids = untis_split_first(class_.teacherids, int)
        owners = [teachers_ref[t_id] for t_id in teacher_ids]

        new_group, created = core_models.Group.objects.get_or_create(
            short_name__iexact=short_name,
            defaults={"name": name, "import_ref": class_.class_id},
        )

        new_group.name = name
        new_group.save()

        new_group.owners.clear()  # configurable
        new_group.owners.add(*owners)

        classes_ref[class_.class_id] = new_group

    return classes_ref


def import_rooms() -> Dict[int, chronos_models.Room]:
    """ Import rooms """

    rooms_ref = {}
    rooms = run_default_filter(mysql_models.Room.objects)
    for room in rooms:
        if not room.name:
            raise Exception("Short name needed.")

        short_name = room.name[:10]
        name = room.longname[:30] if room.longname else short_name

        new_room, created = chronos_models.Room.objects.get_or_create(
            short_name=short_name, defaults={"name": name}
        )

        new_room.name = name
        new_room.save()

        rooms_ref[room.room_id] = new_room

    return rooms_ref


def import_supervision_areas() -> Dict[int, chronos_models.SupervisionArea]:
    """ Import supervision areas """

    supervision_areas_ref = {}
    areas = run_default_filter(mysql_models.Corridor.objects, filter_term=False)
    for area in areas:
        if not area.name:
            raise Exception("Short name needed.")

        short_name = area.name[:10]
        name = area.longname[:50] if area.longname else short_name
        colour_fg = untis_colour_to_hex(area.forecolor)
        colour_bg = untis_colour_to_hex(area.backcolor)

        new_area, created = chronos_models.SupervisionArea.objects.get_or_create(
            short_name=short_name,
            defaults={"name": name, "colour_fg": colour_fg, "colour_bg": colour_bg},
        )

        new_area.name = name
        new_area.colour_fg = colour_fg
        new_area.colour_bg = colour_bg
        new_area.save()

        # TODO: Supervisions

        supervision_areas_ref[area.corridor_id] = new_area

    return supervision_areas_ref


def import_time_periods_and_breaks() -> List[List[chronos_models.TimePeriod]]:
    """ Import time periods an breaks """

    time_periods_ref = []
    periods = (
        run_default_filter(mysql_models.Commondata.objects, filter_term=False)
        .filter(id=40)  # Fixed UNTIS constant
        .order_by("number", "number1")
    )

    for time_period in periods:
        weekday = time_period.number - 1
        period = time_period.number1
        start_time = time(time_period.fieldbyte1, time_period.fieldbyte2)
        end_time = time(time_period.fieldbyte3, time_period.fieldbyte4)

        new_time_period, created = chronos_models.TimePeriod.objects.get_or_create(
            weekday=weekday,
            period=period,
            defaults={"time_start": start_time, "time_end": end_time},
        )

        new_time_period.time_start = start_time
        new_time_period.time_end = end_time
        new_time_period.save()

        # Build index with time periods
        if len(time_periods_ref) < weekday + 1:
            time_periods_ref.append([])
        time_periods_ref[weekday].append(new_time_period)

    # Build breaks for all weekdays
    for weekday, time_periods in enumerate(time_periods_ref):

        # Add None two times in order to create breaks before first lesson and after last lesson
        time_periods = [None] + time_periods + [None]
        for i, time_period in enumerate(time_periods):
            # If last item (None) is reached, no further break must be created
            if i + 1 == len(time_periods):
                break

            after_period = time_period
            before_period = time_periods[i + 1]

            short_name = "{}: {}./{}.".format(
                weekday,
                after_period.period if after_period else "-",
                before_period.period if before_period else "-",
            )

            new_break, created = chronos_models.Break.objects.get_or_create(
                after_period=after_period,
                before_period=before_period,
                defaults={"short_name": short_name, "name": short_name},
            )

    return time_periods_ref
