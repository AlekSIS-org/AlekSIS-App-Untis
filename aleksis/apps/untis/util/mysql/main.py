from .importers.common_data import (
    import_subjects,
    import_classes,
    import_rooms,
    import_supervision_areas,
    import_teachers,
    import_time_periods,
    import_breaks)
from .importers.lessons import import_lessons
from .importers.substitutions import import_substitutions


def untis_import_mysql():
    # Coomon data for Chronos
    subjects_ref = import_subjects()
    rooms_ref = import_rooms()

    # Common data for core
    teachers_ref = import_teachers()
    classes_ref = import_classes(teachers_ref)

    # Time periods
    time_periods_ref = import_time_periods()
    breaks_ref = import_breaks(time_periods_ref)

    # Supervisions
    supervision_areas_ref = import_supervision_areas(breaks_ref, teachers_ref)

    # Lessons
    import_lessons(time_periods_ref, rooms_ref, subjects_ref, teachers_ref, classes_ref)

    # Substitutions
    import_substitutions(teachers_ref, subjects_ref, rooms_ref, classes_ref, supervision_areas_ref)
