import datetime

from django.utils import timezone, formats

from schoolapps.settings import LONG_WEEK_DAYS
from untisconnect.api import TYPE_TEACHER, get_teacher_by_shortcode, TYPE_CLASS, get_class_by_name, get_all_teachers, \
    get_all_classes, get_all_rooms, get_all_subjects
from userinformation import UserInformation


def get_name_for_next_week_day_from_today() -> str:
    """
    Return the next week day as you would say it from today: "today", "tomorrow" or "<weekday>"
    :return: Formatted date
    """
    # Next weekday
    next_weekday: timezone.datetime = get_next_weekday_with_time(timezone.now(), timezone.now().time())

    if next_weekday.date() == timezone.now().date():
        # Today
        date_formatted = "heute"
    elif next_weekday.date() == timezone.now().date() + timezone.timedelta(days=1):
        # Tomorrow
        date_formatted = "morgen"
    else:
        # Other weekday
        date_formatted = LONG_WEEK_DAYS[next_weekday.isoweekday() - 1][0]

    return date_formatted


def get_calendar_weeks(year=timezone.datetime.now().year):
    weeks = []

    # Get first day of year > first calendar week
    first_day_of_year = timezone.datetime(year=year, month=1, day=1)
    if first_day_of_year.isoweekday() != 1:
        days_to_next_monday = 1 - first_day_of_year.isoweekday()
        first_day_of_year += datetime.timedelta(days=days_to_next_monday)

    # Go for all weeks in year and create week dict
    first_day_of_week = first_day_of_year
    for i in range(52):
        calendar_week = i + 1
        last_day_of_week = first_day_of_week + datetime.timedelta(days=4)
        weeks.append({
            "calendar_week": calendar_week,
            "first_day": first_day_of_week,
            "last_day": last_day_of_week
        })
        first_day_of_week += datetime.timedelta(weeks=1)

    return weeks


def find_out_what_is_today(year=None, month=None, day=None):
    date = timezone.datetime.now()
    time = datetime.datetime.now().time()
    if year is not None and day is not None and month is not None:
        date = timezone.datetime(year=year, month=month, day=day)
        if date != timezone.datetime.now():
            time = datetime.time(0)
    return date, time


def get_calendar_week(calendar_week, year=timezone.datetime.now().year):
    weeks = get_calendar_weeks(year=year)
    for week in weeks:
        if week["calendar_week"] == calendar_week:
            return week
    return None


def get_next_weekday(date=None):
    """Get the next weekday by a datetime object"""
    if date is None:
        date = timezone.now().date()

    if date.isoweekday() in {6, 7}:
        if date.isoweekday() == 6:
            plus = 2
        else:
            plus = 1
        date += datetime.timedelta(days=plus)
    return date


def get_next_weekday_with_time(date=None, time=None) -> datetime.datetime:
    """Get the next weekday by a datetime object"""
    if date is None:
        date = timezone.now().date()
    if time is None:
        time = timezone.now().time()

    if time > datetime.time(15, 35):
        date += datetime.timedelta(days=1)
    if date.isoweekday() in {6, 7}:
        if date.isoweekday() == 6:
            plus = 2
        else:
            plus = 1
        date += datetime.timedelta(days=plus)
    return date


def calendar_week(date: datetime) -> int:
    return date.isocalendar()[1]


def weekday(date: datetime) -> int:
    return date.isoweekday() - 1


def format_lesson_time(time: datetime) -> str:
    return formats.date_format(time, "H:i")
