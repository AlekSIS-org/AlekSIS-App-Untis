import logging
from datetime import timedelta

from constance import config
from django.utils.translation import gettext as _
from tqdm import tqdm

from aleksis.apps.chronos import models as chronos_models
from aleksis.core import models as core_models

from .... import models as mysql_models
from ..util import (
    run_default_filter,
    untis_split_third,
    untis_date_to_date,
    get_term,
    sync_m2m,
    compare_m2m,
    connect_untis_fields, TQDM_DEFAULTS,
)

logger = logging.getLogger(__name__)


def import_lessons(
    time_periods_ref, rooms_ref, subjects_ref, teachers_ref, classes_ref
):
    """ Import lessons """

    # Get current term
    term = get_term()
    date_start = untis_date_to_date(term.datefrom)
    date_end = untis_date_to_date(term.dateto)

    # Get all existing lessons for this term
    lessons_in_term = chronos_models.Lesson.objects.filter(
        term_untis=term.term_id
    ).values_list("id", flat=True)

    # Set the end date of all lessons from other terms ending in this term to the day before this term starts
    chronos_models.Lesson.objects.filter(date_end__gte=date_start).exclude(
        id__in=lessons_in_term
    ).update(date_end=date_start - timedelta(days=1))

    # Lessons
    lessons = run_default_filter(mysql_models.Lesson.objects)
    for lesson in tqdm(lessons, desc="Import lessons", **TQDM_DEFAULTS):
        lesson_id = lesson.lesson_id

        logger.info(_("Import lesson {}").format(lesson_id))

        if not lesson.lesson_tt:
            logger.warning(_("  Skip because missing times").format(lesson_id))
            continue

        # Split data (,)
        raw_lesson_data = connect_untis_fields(lesson, "lessonelement", 10)
        raw_time_data = lesson.lesson_tt.split(",")

        raw_time_data_2 = []
        for el in raw_time_data:
            # Split data (~)
            raw_time_data_2.append(el.split("~"))

        # Get time periods and rooms
        time_periods = []
        rooms_per_periods = []
        for el in raw_time_data_2:
            weekday = int(el[1]) - 1
            hour = int(el[2])
            room_ids = untis_split_third(el[3], conv=int)

            # Get rooms
            rooms = []
            for room_id in room_ids:
                r = rooms_ref[room_id]
                rooms.append(r)

            # Get time period
            time_period = time_periods_ref[weekday][hour]
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

            teachers = [teacher] if teacher else []

            # Get subject
            if subject_id != 0:
                subject = subjects_ref[subject_id]
            else:
                logger.warning(_("    Skip because missing subject".format(i)))
                continue

            # Get classes
            course_classes = []
            for class_id in class_ids:
                c = classes_ref[class_id]
                course_classes.append(c)

            if config.UNTIS_IMPORT_MYSQL_USE_COURSE_GROUPS:
                group_import_ref = -int("{}{}".format(lesson_id, i))
                subject_ref = subject.abbrev

                # Search by parent groups and subject
                qs = core_models.Group.objects.filter(
                    parent_groups__in=[c.id for c in course_classes],
                    untis_subject__iexact=subject_ref,
                )

                # Check if found groups match
                match = False
                if qs.exists():
                    if compare_m2m(course_classes, qs[0].parent_groups.all()):
                        match = True
                        course_group = qs[0]
                        logger.info(
                            "    Course group found by searching by parent groups and subject"
                        )

                changed = False
                if not match:
                    # No matching group found

                    # Build names and refs for course groups
                    group_short_name = "{}-{}".format(
                        "".join([c.short_name for c in course_classes]), subject.abbrev
                    )
                    group_name = "{}: {}".format(
                        ", ".join([c.short_name for c in course_classes]),
                        subject.abbrev,
                    )

                    # Get or create course group
                    course_group, created = core_models.Group.objects.get_or_create(
                        short_name=group_short_name, defaults={"name": group_name}
                    )

                    # Log
                    if created:
                        logger.info("    Course group created")

                    # Update parent groups
                    sync_m2m(course_classes, course_group.parent_groups)

                    # Update name
                    if course_group.name != group_name:
                        course_group.name = group_name
                        logger.info("    Name of course group updated")

                        changed = True

                # Update owners
                sync_m2m(teachers, course_group.owners)

                # Update import ref
                if (
                    course_group.import_ref_untis != group_import_ref
                ):  # or course_group.untis_subject != subject_ref:
                    course_group.import_ref_untis = group_import_ref
                    # course_group.subject_ref = subject_ref
                    logger.info("    Import reference of course group updated")
                    changed = True

                if changed:
                    course_group.save()

                groups = [course_group]
            else:
                groups = course_classes

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
            sync_m2m(groups, lesson.groups)

            # Sync teachers
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
