import logging

from aleksis.apps.chronos import models as chronos_models

from .... import models as mysql_models
from ..util import (
    run_default_filter,
    get_term,
    untis_date_to_date,
)

logger = logging.getLogger(__name__)
unknown_reason, _ = chronos_models.AbsenceReason.objects.get_or_create(short_name="?")


def import_absences(
    absence_reasons_ref, time_periods_ref, teachers_ref, classes_ref, rooms_ref
):
    ref = {}

    # Get term
    term = get_term()
    term_date_start = untis_date_to_date(term.datefrom)
    term_date_end = untis_date_to_date(term.dateto)

    # Get absences
    absences = (
        run_default_filter(mysql_models.Absence.objects, filter_term=False)
        .filter(datefrom__lte=term.dateto, dateto__gte=term.datefrom)
        .order_by("absence_id")
    )

    existing_absences = []
    for absence in absences:
        import_ref = absence.absence_id

        logger.info("Import absence {}".format(import_ref))

        if absence.absence_reason_id == 0:
            logger.warning("  Absence reason needed")
            reason = unknown_reason
        else:
            reason = absence_reasons_ref[absence.absence_reason_id]

        # Build values
        type_ = absence.typea
        date_from = untis_date_to_date(absence.datefrom)
        date_to = untis_date_to_date(absence.dateto)
        period_from = absence.lessonfrom
        period_to = absence.lessonto
        weekday_from = date_from.weekday()
        weekday_to = date_to.weekday()

        # Check min/max weekdays
        first_weekday = sorted(time_periods_ref.keys())[0]
        last_weekday = sorted(time_periods_ref.keys())[-1]

        if weekday_from < first_weekday:
            weekday_from = first_weekday
        if weekday_from > last_weekday:
            weekday_from = last_weekday
        if weekday_to < first_weekday:
            weekday_to = first_weekday
        if weekday_to > last_weekday:
            weekday_to = last_weekday

        # Check min/max periods
        first_period = sorted(time_periods_ref[first_weekday].keys())[0]
        last_period = sorted(time_periods_ref[first_weekday].keys())[-1]

        if period_from == 0:
            period_from = first_period
        if period_to == 0:
            period_to = last_period

        time_period_from = time_periods_ref[weekday_from][period_from]
        time_period_to = time_periods_ref[weekday_to][period_to]
        comment = absence.text

        group = None
        teacher = None
        room = None

        # 100, 101 and 102 are UNTIS constants
        if type_ == 100:
            group = classes_ref[absence.ida]
        elif type_ == 101:
            teacher = teachers_ref[absence.ida]
        elif type == 102:
            room = rooms_ref[absence.ida]

        new_absence, created = chronos_models.Absence.objects.get_or_create(
            import_ref_untis=import_ref,
            defaults={
                "reason": reason,
                "group": group,
                "teacher": teacher,
                "room": room,
                "date_start": date_from,
                "date_end": date_to,
                "period_from": time_period_from,
                "period_to": time_period_to,
                "comment": absence.text,
            },
        )

        if created:
            logger.info("  New absence created")

        if (
            new_absence.reason != reason
            or new_absence.group != group
            or new_absence.teacher != teacher
            or new_absence.room != room
            or new_absence.date_start != date_from
            or new_absence.date_end != date_to
            or new_absence.period_from != time_period_from
            or new_absence.period_to != time_period_to
            or new_absence.comment != comment
        ):
            new_absence.reason = reason
            new_absence.group = group
            new_absence.teacher = teacher
            new_absence.room = room
            new_absence.date_start = date_from
            new_absence.date_end = date_to
            new_absence.period_from = time_period_from
            new_absence.period_to = time_period_to
            new_absence.comment = comment
            new_absence.save()
            logger.info("  Absence updated")

        existing_absences.append(import_ref)
        ref[import_ref] = new_absence

        # Delete all no longer existing absences
        for a in chronos_models.Absence.objects.filter(
            date_start__lte=term_date_start, date_end__gte=term_date_end
        ):
            if a.import_ref_untis and a.import_ref_untis not in existing_absences:
                logger.info("Absence {} deleted".format(a.id))
                a.delete()
