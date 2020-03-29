from datetime import date, datetime
from typing import Optional

from django.db.models import QuerySet

from aleksis.apps.untis import models as mysql_models

DB_NAME = "untis"


def run_using(obj: QuerySet) -> QuerySet:
    return obj.using(DB_NAME)


def get_term(date: Optional[date] = None) -> mysql_models.Terms:
    """ Get term valid for the provided date """

    if not date:
        date = datetime.now()

    terms = run_using(mysql_models.Terms.objects).filter(
        datefrom__lte=date_to_untis_date(date), dateto__gte=date_to_untis_date(date)
    )

    if not terms.exists():
        raise Exception("Term needed")

    return terms[0]


def run_default_filter(
    qs: QuerySet, date: Optional[date] = None, filter_term: bool = True
) -> QuerySet:
    """ Add a default filter in order to select the correct term """

    term = get_term(date)
    term_id, schoolyear_id, school_id, version_id = (
        term.term_id,
        term.schoolyear_id,
        term.school_id,
        term.version_id,
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


def clean_array(a: list, conv=None) -> list:
    b = []
    for el in a:
        if el != "" and el != "0":
            if conv is not None:
                el = conv(el)
            b.append(el)
    return b


def untis_split_first(s: str, conv=None) -> list:
    return clean_array(s.split(","), conv=conv)


def untis_split_second(s: str, conv=None) -> list:
    return clean_array(s.split("~"), conv=conv)


def untis_split_third(s: str, conv=None) -> list:
    return clean_array(s.split(";"), conv=conv)


UNTIS_DATE_FORMAT = "%Y%m%d"


def untis_date_to_date(untis: int) -> date:
    """ Converts a UNTIS date to a python date """
    return datetime.strptime(str(untis), UNTIS_DATE_FORMAT).date()


def date_to_untis_date(date: date) -> int:
    """ Converts a python date to a UNTIS date """
    return int(date.strftime(UNTIS_DATE_FORMAT))


def untis_colour_to_hex(colour: int) -> str:
    # Convert UNTIS number to HEX
    hex_bgr = str(hex(colour)).replace("0x", "")

    # Add beginning zeros if len < 6
    if len(hex_bgr) < 6:
        hex_bgr = "0" * (6 - len(hex_bgr)) + hex_bgr

    # Change BGR to RGB
    hex_rgb = hex_bgr[4:6] + hex_bgr[2:4] + hex_bgr[0:2]

    # Add html #
    return "#" + hex_rgb
