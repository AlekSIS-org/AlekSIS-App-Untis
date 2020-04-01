import logging

from django.utils.translation import gettext as _

from aleksis.apps.chronos import models as chronos_models
from aleksis.core import models as core_models
from aleksis.core.util import messages

from .... import models as mysql_models
from ..util import run_default_filter, untis_split_third, untis_date_to_date, get_term

logger = logging.getLogger(__name__)


def sync_m2m(new_items, m2m_qs):
    for item in new_items:
        if item not in m2m_qs.all():
            m2m_qs.add(item)
            logger.info("  Many-to-many sync: item added")
    for item in m2m_qs.all():
        if item not in new_items:
            m2m_qs.remove(item)
            logger.info("  Many-to-many sync: item removed")


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
                None, message=_("  Skip because missing times").format(lesson_id),
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
            logger.info("  Lesson part {}".format(i))

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
                    None, message=_("    Skip because missing subject".format(i)),
                )
                continue

            # Get classes
            course_classes = []
            for class_id in class_ids:
                c = classes_ref[class_id]
                course_classes.append(c)

            # Build names and refs for course groups
            group_short_name = "{}-{}".format(
                "".join([c.short_name for c in course_classes]), subject.abbrev
            )
            group_name = "{}: {}".format(
                ", ".join([c.short_name for c in course_classes]), subject.abbrev
            )
            group_import_ref = -int("{}{}".format(lesson_id, i))

            # Get or create course group
            course_group, created = core_models.Group.objects.get_or_create(
                short_name=group_short_name, defaults={"name": group_name}
            )
            course_group.import_ref_untis = group_import_ref
            course_group.name = group_name
            course_group.save()
            course_group.parent_groups.set(course_classes)

            if created:
                logger.info("    Course group created")

            # Create new lesson
            date_start = untis_date_to_date(term.datefrom)
            date_end = untis_date_to_date(term.dateto)

            # Get old lesson
            old_lesson_qs = chronos_models.Lesson.objects.filter(
                lesson_id_untis=lesson_id, element_id_untis=i, term_untis=term.term_id
            )

            if old_lesson_qs.exists():
                # Update existing lesson
                logger.info("    Existing lesson found")

                old_lesson = old_lesson_qs[0]

                if (
                    old_lesson.subject != subject
                    or old_lesson.date_start != date_start
                    or old_lesson.date_end != date_end
                ):
                    old_lesson.subject = subject
                    old_lesson.date_start = date_start
                    old_lesson.date_end = date_end
                    old_lesson.save()
                    logger.info("    Subject, start date and end date updated")
                lesson = old_lesson
            else:
                # Create new lesson

                lesson = chronos_models.Lesson.objects.create(
                    subject=subject,
                    date_start=date_start,
                    date_end=date_end,
                    lesson_id_untis=lesson_id,
                    element_id_untis=i,
                    term_untis=term.term_id,
                )
                logger.info("    New lesson created")

            # Sync groups
            groups = [course_group]
            sync_m2m(groups, lesson.groups)

            # Sync teachers
            teachers = [teacher] if teacher else []
            sync_m2m(teachers, lesson.teachers)

            # All times for this course
            old_lesson_periods_qs = chronos_models.LessonPeriod.objects.filter(
                lesson=lesson
            )

            # If length has changed, delete all lesson periods
            if old_lesson_periods_qs.count() != len(time_periods):
                old_lesson_periods_qs.delete()
                logger.info("    Lesson periods deleted")

            # Sync time periods
            for j, time_period in enumerate(time_periods):
                logger.info("    Import lesson period {}".format(time_period))

                # Get room if provided
                rooms = rooms_per_periods[j]
                if i < len(rooms):
                    room = rooms[i]
                else:
                    room = None

                # Check if an old lesson period is provided
                old_lesson_period_qs = old_lesson_periods_qs.filter(element_id_untis=j)
                if old_lesson_period_qs.exists():
                    # Update old lesson period

                    old_lesson_period = old_lesson_period_qs[0]
                    if (
                        old_lesson_period.period != time_period
                        or old_lesson_period.room != room
                    ):
                        old_lesson_period.period = time_period
                        old_lesson_period.room = room
                        old_lesson_period.save()
                        logger.info("      Time period and room updated")
                else:
                    # Create new lesson period

                    lesson.periods.add(
                        time_period,
                        through_defaults={"room": room, "element_id_untis": j},
                    )
                    logger.info("      New time period added")
