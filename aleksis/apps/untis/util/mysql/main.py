from .importers.common_data import (
    import_subjects,
    import_classes,
    import_rooms,
    import_supervision_areas,
    import_teachers,
    import_time_periods_and_breaks,
)
from .importers.lessons import import_lessons


def untis_import_mysql():
    # Coomon data for Chronos
    subjects_ref = import_subjects()
    rooms_ref = import_rooms()
    supervision_areas_ref = import_supervision_areas()

    # Common data for core
    teachers_ref = import_teachers()
    classes_ref = import_classes(teachers_ref)

    # Time periods
    time_periods_ref = import_time_periods_and_breaks()

    # Lessons
    import_lessons(time_periods_ref, rooms_ref, subjects_ref, teachers_ref, classes_ref)
