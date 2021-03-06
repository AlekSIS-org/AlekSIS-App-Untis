import logging
from datetime import date
from typing import Dict, Optional

from django.db.models import QuerySet
from django.utils import timezone

from tqdm import tqdm

from aleksis.apps.chronos import models as chronos_models
from aleksis.apps.untis.util.mysql.util import (
    TQDM_DEFAULTS,
    date_to_untis_date,
    run_using,
    untis_date_to_date,
)
from aleksis.core import models as core_models

from .... import models as mysql_models


def get_terms_for_date(for_date: Optional[date] = None) -> QuerySet:
    """Get term queryset with term valid for the provided date."""
    if not for_date:
        for_date = timezone.now().date()

    qs = run_using(mysql_models.Terms.objects).filter(
        datefrom__lte=date_to_untis_date(for_date), dateto__gte=date_to_untis_date(for_date),
    )

    return qs


def get_future_terms_for_date(for_date: Optional[date] = None) -> QuerySet:
    """Get all furture terms (after the current term)."""
    if not for_date:
        for_date = timezone.now().date()

    qs = run_using(mysql_models.Terms.objects).filter(datefrom__gt=date_to_untis_date(for_date),)

    return qs


logger = logging.getLogger(__name__)


def import_terms(qs: Optional[QuerySet] = None,) -> Dict[int, chronos_models.ValidityRange]:
    """Import terms and school years as validity ranges and school terms."""
    ranges_ref = {}

    if not isinstance(qs, QuerySet):
        qs = run_using(mysql_models.Terms.objects).all()

    school_terms = {}
    for term in tqdm(qs, desc="Import terms (as validity ranges)", **TQDM_DEFAULTS):
        if not term.name:
            raise RuntimeError(
                "Term ID {}: Cannot import term without short name.".format(term.term_id)
            )
        term_id = term.term_id
        name = term.longname if term.longname else term.name
        date_start = untis_date_to_date(term.datefrom)
        date_end = untis_date_to_date(term.dateto)

        logger.info(f"Import term {term_id} ({date_start}–{date_end})")

        school_year_id = term.schoolyear_id
        try:
            school_term = core_models.SchoolTerm.objects.within_dates(date_start, date_end).get()
            logger.info("    School term found by time.")
        except core_models.SchoolTerm.DoesNotExist:
            if school_year_id in school_terms:
                school_term = school_terms[school_year_id]
                logger.info(f"  School year {school_year_id} already there.")
            else:
                school_year = run_using(mysql_models.Schoolyear.objects).get(
                    schoolyear_id=school_year_id
                )
                school_term_name = (
                    school_year.text if school_year.text else school_year.schoolyearzoned
                )

                logger.info(f"  Import school year {school_year_id} ...")

                try:
                    school_term = core_models.SchoolTerm.objects.get(
                        import_ref_untis=school_year_id
                    )
                    logger.info("    School year found by import reference.")
                except core_models.SchoolTerm.DoesNotExist:
                    school_term = core_models.SchoolTerm(
                        date_start=date_start, date_end=date_end, name=school_term_name
                    )
                    logger.info("    School year created newly.")

            school_term.import_ref_untis = school_year_id

        if school_term.date_end < date_end:
            school_term.date_end = date_end

        if school_term.date_start > date_start:
            school_term.date_start = date_start

        school_term.save()

        try:
            validity_range = chronos_models.ValidityRange.objects.get(import_ref_untis=term_id)
            logger.info("  Validity range found by import reference.")
        except chronos_models.ValidityRange.DoesNotExist:
            try:
                validity_range = chronos_models.ValidityRange.objects.within_dates(
                    date_start, date_end
                ).get()
                logger.info("  Validity range found by time.")
            except chronos_models.ValidityRange.DoesNotExist:
                validity_range = chronos_models.ValidityRange()
                logger.info("  Validity range created newly.")

        validity_range.import_ref_untis = term_id
        validity_range.date_start = date_start
        validity_range.date_end = date_end
        validity_range.name = name
        validity_range.school_term = school_term
        validity_range.school_year_untis = school_year_id
        validity_range.school_id_untis = term.school_id
        validity_range.version_id_untis = term.version_id

        validity_range.save()

        ranges_ref[validity_range] = validity_range

    return ranges_ref
