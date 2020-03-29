from datetime import datetime, date, time

from django.db.models import Model, QuerySet
from django.utils.translation import gettext as _
from aleksis.apps.untis import models as mysql_models
from aleksis.apps.untis.util.mysql.api_helper import (
    date_to_untis_date,
    untis_colour_to_hex,
    untis_split_first,
    untis_split_third,
    untis_date_to_date,
)

from aleksis.apps.chronos import models as chronos_models
from aleksis.core import models as core_models
from aleksis.core.util import messages

DB_NAME = "untis"


def run_using(obj):
    return obj.using(DB_NAME)


TERM: mysql_models.Terms = None


def run_default_filter(qs: QuerySet, filter_term: bool = True) -> QuerySet:
    """ Add a default filter in order to select the correct term """
    global TERM
    term_id, schoolyear_id, school_id, version_id = (
        TERM.term_id,
        TERM.schoolyear_id,
        TERM.school_id,
        TERM.version_id,
    )

    if filter_term:
        return run_using(qs).filter(
            school_id=school_id,
            schoolyear_id=schoolyear_id,
            version_id=version_id,
            term_id=term_id,
        )
    else:
        return run_using(qs).filter(
            school_id=school_id, schoolyear_id=schoolyear_id, version_id=version_id
        )


def get_term(date: date) -> mysql_models.Terms:
    """ Get term valid for the provided date """

    terms = run_using(mysql_models.Terms.objects).filter(
        datefrom__lte=date_to_untis_date(date), dateto__gte=date_to_untis_date(date)
    )

    if not terms.exists():
        raise Exception("Term needed")

    return terms[0]


def untis_import_mysql():
    global TERM
    date = datetime.now().date()
    TERM = get_term(date)

    # Subjects
    subjects_ref = {}
    subjects = run_default_filter(mysql_models.Subjects.objects, filter_term=False)
    for subject in subjects:
        if not subject.name:
            raise Exception("Short name needed.")

        short_name = subject.name[:10]
        name = subject.longname if subject.longname else short_name

        new_subject, created = chronos_models.Subject.objects.get_or_create(
            abbrev=short_name, defaults={"name": name}
        )

        new_subject.name = name
        new_subject.colour_fg = untis_colour_to_hex(subject.forecolor)
        new_subject.colour_bg = untis_colour_to_hex(subject.backcolor)
        new_subject.save()

        subjects_ref[subject.subject_id] = new_subject

    # Teachers
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

    # Classes
    classes_ref = {}
    classes = run_default_filter(mysql_models.Class.objects, filter_term=True)

    for class_ in classes:
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

    # Rooms
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

    # SupervisionArea
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

    # Time Periods
    time_periods_ref = []
    periods = run_default_filter(
        mysql_models.Commondata.objects, filter_term=False
    ).filter(
        id=40 # Fixed UNTIS constant
    ).order_by("number", "number1")

    for time_period in periods:
        weekday = time_period.number - 1
        period = time_period.number1
        start_time = time(time_period.fieldbyte1, time_period.fieldbyte2)
        end_time = time(time_period.fieldbyte3, time_period.fieldbyte4)

        new_time_period, created = chronos_models.TimePeriod.objects.get_or_create(
            weekday=weekday, period=period,
            defaults={"time_start": start_time, "time_end": end_time}
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

            short_name = "{}: {}./{}.".format(weekday, after_period.period if after_period else "-", before_period.period if before_period else "-")

            new_break, created = chronos_models.Break.objects.get_or_create(
                after_period=after_period,
                before_period=before_period,
                defaults={
                    "short_name": short_name,
                    "name": short_name
                }
            )

    # Lessons
    lessons = run_default_filter(mysql_models.Lesson.objects)
    for lesson in lessons:
        lesson_id = lesson.lesson_id

        messages.info(None, message=_("Import lesson {}").format(lesson_id))

        if not lesson.lesson_tt:
            messages.warning(
                None,
                message=_("Skip lesson {} because there are missing times.").format(
                    lesson_id
                ),
            )
            continue

        # Split data (,)
        raw_lesson_data = lesson.lessonelement1.split(",")
        raw_time_data = lesson.lesson_tt.split(",")

        raw_time_data_2 = []
        for el in raw_time_data:
            # Split data (~)
            raw_time_data_2.append(el.split("~"))

        # Get time periods and rooms
        time_periods = []
        rooms_per_periods = []
        for el in raw_time_data_2:
            day = int(el[1])
            hour = int(el[2])
            room_ids = untis_split_third(el[3], conv=int)

            # Get rooms
            rooms = []
            for room_id in room_ids:
                r = rooms_ref[room_id]
                rooms.append(r)

            # Get time period
            time_period = time_periods_ref[day - 1][hour - 1]
            time_periods.append(time_period)
            rooms_per_periods.append(rooms)

        # Split data more (~)
        raw_lesson_data_2 = []
        for el in raw_lesson_data:
            raw_lesson_data_2.append(el.split("~"))

        # All part lessons (courses)
        for i, el in enumerate(raw_lesson_data_2):
            # Get plain ids
            teacher_id = int(el[0])
            subject_id = int(el[2])
            class_ids = untis_split_third(el[17], conv=int)

            # Get teacher
            if teacher_id != 0:
                teacher = teachers_ref[teacher_id]
            else:
                teacher = None

            # Get subject
            if subject_id != 0:
                subject = subjects_ref[subject_id]
            else:
                messages.warning(
                    None,
                    message=_(
                        "Skip lesson {}, element {} because there is missing a subject.".format(
                            lesson_id, i
                        )
                    ),
                )
                continue
                # raise Exception("Subject needed.")

            # Get classes
            course_classes = []
            for class_id in class_ids:
                c = classes_ref[class_id]
                course_classes.append(c)

            # Build names and refs for course groups
            short_name = "{}-{}".format(
                "".join([c.short_name for c in course_classes]), subject.abbrev
            )
            name = "{}: {}".format(
                ", ".join([c.short_name for c in course_classes]), subject.abbrev
            )
            import_ref = "{}-{}".format(lesson_id, i)

            # Get or create course group
            course_group, created = core_models.Group.objects.get_or_create(
                short_name=short_name, defaults={"name": name}
            )
            course_group.import_ref = import_ref
            course_group.name = name

            course_group.save()
            course_group.parent_groups.set(course_classes)

            # Create new lesson
            date_start = untis_date_to_date(TERM.datefrom)
            date_end = untis_date_to_date(TERM.dateto)
            lesson = chronos_models.Lesson.objects.create(
                subject=subject, date_start=date_start, date_end=date_end
            )

            # Set groups
            lesson.groups.set([course_group])

            # Set teacher
            if teacher:
                lesson.teachers.set([teacher])

            # All times for this course
            for j, time_period in enumerate(time_periods):
                rooms = rooms_per_periods[j]

                if i < len(rooms):
                    lesson.periods.add(time_period, through_defaults={"room": rooms[i]})
                else:
                    lesson.periods.add(time_period)
