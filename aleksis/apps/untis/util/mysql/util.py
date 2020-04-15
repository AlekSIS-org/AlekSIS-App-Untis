import logging
from datetime import date, datetime
from typing import Optional, Union, List

from django.db.models import QuerySet, Model

from aleksis.apps.untis import models as mysql_models

DB_NAME = "untis"

logger = logging.getLogger(__name__)


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
    qs: QuerySet, date: Optional[date] = None, filter_term: bool = True, filter_deleted: bool = True
) -> QuerySet:
    """ Add a default filter in order to select the correct term """

    term = get_term(date)
    term_id, schoolyear_id, school_id, version_id = (
        term.term_id,
        term.schoolyear_id,
        term.school_id,
        term.version_id,
    )

    qs = run_using(qs).filter(
            school_id=school_id,
            schoolyear_id=schoolyear_id,
            version_id=version_id,
    )

    if filter_term:
        qs = qs.filter(term_id=term_id)

    if filter_deleted:
        qs = qs.filter(deleted=0)

    return qs


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


def sync_m2m(new_items: Union[List[Model], QuerySet], m2m_qs: QuerySet):
    """ Sync m2m field """

    # Add items
    for item in new_items:
        if item not in m2m_qs.all():
            m2m_qs.add(item)
            logger.info("  Many-to-many sync: item added")

    # Delete items
    for item in m2m_qs.all():
        if item not in new_items:
            m2m_qs.remove(item)
            logger.info("  Many-to-many sync: item removed")


def compare_m2m(
    a: Union[List[Model], QuerySet], b: Union[List[Model], QuerySet]
) -> bool:
    """ Compare if content of two m2m fields is equal """

    ids_a = sorted([i.id for i in a])
    ids_b = sorted([i.id for i in b])
    return ids_a == ids_b


def connect_untis_fields(obj: Model, attr: str, limit: int) -> List[str]:
    """ Connects data from multiple DB fields """

    all_data = []

    for i in range(1, limit + 1):
        attr_name = "{}{}".format(attr, i)
        raw_data = getattr(obj, attr_name, "")
        if raw_data not in ("", None):
            data = untis_split_first(raw_data)
            all_data += data

    return all_data


def get_first_weekday(time_periods_ref: dict) -> int:
    """ Get first weekday from time periods reference """
    return sorted(time_periods_ref.keys())[0]


def get_last_weekday(time_periods_ref: dict) -> int:
    """ Get last weekday from time periods reference """
    return sorted(time_periods_ref.keys())[-1]


def get_first_period(time_periods_ref: dict, weekday: int) -> int:
    """ Get first period on a weekday from time periods reference """
    return sorted(time_periods_ref[weekday].keys())[0]


def get_last_period(time_periods_ref: dict, weekday: int) -> int:
    """ Get last period an a weekday from time periods reference """
    return sorted(time_periods_ref[weekday].keys())[-1]


def move_weekday_to_range(time_periods_ref: dict, weekday: int) -> int:
    """ Move weekday values into school week (e. g. saturday to friday) """
    first_weekday = get_first_weekday(time_periods_ref)
    last_weekday = get_last_weekday(time_periods_ref)

    if weekday < first_weekday:
        weekday = first_weekday
    if weekday > last_weekday:
        weekday = last_weekday

    return weekday
