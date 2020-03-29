from django.utils.translation import gettext as _

from aleksis.apps.chronos import models as chronos_models
from aleksis.core import models as core_models
from aleksis.core.util import messages

from .... import models as mysql_models
from ..util import run_default_filter, untis_split_third, untis_date_to_date, get_term


def import_lessons(
    time_periods_ref, rooms_ref, subjects_ref, teachers_ref, classes_ref
):
    """ Import lessons """

    # Get current term
    term = get_term()

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
            date_start = untis_date_to_date(term.datefrom)
            date_end = untis_date_to_date(term.dateto)
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
