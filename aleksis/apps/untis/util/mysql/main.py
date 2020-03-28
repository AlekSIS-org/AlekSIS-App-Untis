from datetime import datetime, date

from django.db.models import Model, QuerySet

from aleksis.apps.untis import models as mysql_models
from aleksis.apps.untis.util.mysql.api_helper import (
    date_to_untis_date,
    untis_colour_to_hex,
)

from aleksis.apps.chronos import models as chronos_models
from aleksis.core import models as core_models

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

    # Teachers
    teachers = run_default_filter(mysql_models.Teacher.objects)
    for teacher in teachers:
        if not teacher.name:
            raise Exception("Short name needed.")

        short_name = teacher.name[:5]
        first_name = teacher.firstname if teacher.firstname else "?"
        last_name = teacher.longname if teacher.longname else teacher.name

        new_teacher, created = core_models.Person.objects.get_or_create(
            short_name=short_name,
            defaults={"first_name": first_name, "last_name": last_name},
        )
