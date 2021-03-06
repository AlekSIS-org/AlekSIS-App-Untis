Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_,
and this project adheres to `Semantic Versioning`_.

`2.0rc1`_ - 2021-06-23
----------------------

Fixed
~~~~~

* Preference section verbose names were displayed in server language and not
  user language (fixed by using gettext_lazy).

`2.0b0`_ - 2021-05-21
---------------------

Added
~~~~~
* Import data related to school terms and validity ranges.
* Provide different Celery tasks for multiple import scenarios.

Changed
~~~~~~~
* Rename permission rules to differentiate from internal permissions.

Fixed
~~~~~
* Cleanly delete old break supervisions instead of just replacing them.
* Do not import lessons without lesson periods.
* Delete (supervision) substitutions which are out of their validity range.
* Only import supervisions for the linked UNTIS term and not for all terms.
* Import supervisions linked to a validity range.
* Import absences with correct absence types and not None values.
* Set teachers to an empty list if there are no original and no substitution teachers.
* Call update_or_create without prefetched or joined data.

Removed
~~~~~~~
* Remove support for XML import due to a lack of maintenance.

`2.0a2`_ - 2020-05-04
---------------------

Added
~~~~~

* Import UNTIS data from MySQL
 * Import absence reasons
 * Import absences
 * Import breaks
 * Import classes
 * Import events
 * Import holidays
 * Import lessons
 * Import rooms
 * Import subjects
 * Import substitutions
 * Import supervision areas
 * Import teachers
 * Import time periods


`1.0a1`_ - 2019-09-17
---------------------

Added
~~~~~

* Allow updating subjects, rooms and time periods from new import
* Allow importing a new version of a timetable

Changed
~~~~~~~

* Use bootstrap buttons everywhere

Fixed
~~~~~

* Work around bug in Untis that wrongly splits classes if they contain
  spaces

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

.. _1.0a1: https://edugit.org/Teckids/AlekSIS/AlekSIS-App-Untis/-/tags/1.0a1
.. _2.0a2: https://edugit.org/Teckids/AlekSIS/AlekSIS-App-Untis/-/tags/2.0a2
.. _2.0b0: https://edugit.org/Teckids/AlekSIS/AlekSIS-App-Untis/-/tags/2.0b0
.. _2.0rc1: https://edugit.org/Teckids/AlekSIS/AlekSIS-App-Untis/-/tags/2.0rc1
