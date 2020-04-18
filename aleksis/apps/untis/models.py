# pylint: skip-file
# flake8: noqa

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from aleksis.core.mixins import PureDjangoModel


class Absence(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    absence_id = models.IntegerField(db_column='ABSENCE_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    typea = models.SmallIntegerField(db_column='TypeA', blank=True, null=True)  # Field name made lowercase.
    ida = models.IntegerField(db_column='IDA', blank=True, null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    absence_reason_id = models.IntegerField(db_column='ABSENCE_REASON_ID', blank=True,
                                            null=True)  # Field name made lowercase.
    lessonfrom = models.SmallIntegerField(db_column='LessonFrom', blank=True, null=True)  # Field name made lowercase.
    lessonto = models.SmallIntegerField(db_column='LessonTo', blank=True, null=True)  # Field name made lowercase.
    transfer_id = models.IntegerField(db_column='TRANSFER_ID', blank=True, null=True)  # Field name made lowercase.
    event_id = models.IntegerField(db_column='EVENT_ID', blank=True, null=True)  # Field name made lowercase.
    valuededuction = models.IntegerField(db_column='ValueDeduction', blank=True,
                                         null=True)  # Field name made lowercase.
    prebookingnr = models.IntegerField(db_column='PrebookingNr', blank=True, null=True)  # Field name made lowercase.
    timefrom = models.IntegerField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.IntegerField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Absence'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'absence_id'),)


class Absencereason(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    absence_reason_id = models.IntegerField(db_column='ABSENCE_REASON_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AbsenceReason'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'absence_reason_id'),)


class Adminlesson(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    ls_id = models.IntegerField(db_column='LS_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    startdate = models.IntegerField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.IntegerField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    studentgroupid = models.IntegerField(db_column='StudentGroupId', blank=True,
                                         null=True)  # Field name made lowercase.
    classids = models.CharField(db_column='ClassIds', max_length=600, blank=True,
                                null=True)  # Field name made lowercase.
    teacherassignments = models.TextField(db_column='TeacherAssignments', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdminLesson'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'ls_id'),)


class Alias(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    alias_id = models.IntegerField(db_column='ALIAS_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    elementids = models.CharField(db_column='ElementIds', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alias'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'type', 'alias_id', 'term_id'),)


class CvReason(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    cv_reason_id = models.IntegerField(db_column='CV_REASON_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_Reason'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'cv_reason_id'),)


class Calendar(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    date = models.IntegerField(db_column='Date')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=150, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    absence_reason_id = models.IntegerField(db_column='ABSENCE_REASON_ID', blank=True,
                                            null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=150, blank=True, null=True)  # Field name made lowercase.
    freelessons = models.CharField(db_column='FreeLessons', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    daytext = models.CharField(db_column='DayText', max_length=2000, blank=True,
                               null=True)  # Field name made lowercase.
    elementids = models.CharField(db_column='ElementIds', max_length=2000, blank=True,
                                  null=True)  # Field name made lowercase.
    textguid = models.CharField(db_column='TextGuid', max_length=2000, blank=True,
                                null=True)  # Field name made lowercase.
    additionaldays = models.CharField(db_column='AdditionalDays', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendar'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'date'),)


class Class(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    class_id = models.IntegerField(db_column='CLASS_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    statisticcodes2 = models.CharField(db_column='StatisticCodes2', max_length=10, blank=True,
                                       null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timerequest = models.CharField(db_column='TimeRequest', max_length=400, blank=True,
                                   null=True)  # Field name made lowercase.
    timerequestminut = models.CharField(db_column='TimeRequestMinut', max_length=400, blank=True,
                                        null=True)  # Field name made lowercase.
    dayrequest = models.CharField(db_column='DayRequest', max_length=400, blank=True,
                                  null=True)  # Field name made lowercase.
    timerequestunspecified = models.CharField(db_column='TimeRequestUnspecified', max_length=400, blank=True,
                                              null=True)  # Field name made lowercase.
    selmatrix = models.CharField(db_column='SelMatrix', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID', blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    minutbreakmin = models.SmallIntegerField(db_column='MinutBreakMin', blank=True,
                                             null=True)  # Field name made lowercase.
    lunchbreakmin = models.SmallIntegerField(db_column='LunchBreakMin', blank=True,
                                             null=True)  # Field name made lowercase.
    lunchbreakmax = models.SmallIntegerField(db_column='LunchBreakMax', blank=True,
                                             null=True)  # Field name made lowercase.
    lssnperdaymin = models.SmallIntegerField(db_column='LssnPerDayMin', blank=True,
                                             null=True)  # Field name made lowercase.
    lssnperdaymax = models.SmallIntegerField(db_column='LssnPerDayMax', blank=True,
                                             null=True)  # Field name made lowercase.
    minutminutesperdaymin = models.SmallIntegerField(db_column='MinutMinutesPerDayMin', blank=True,
                                                     null=True)  # Field name made lowercase.
    minutminutesperdaymax = models.SmallIntegerField(db_column='MinutMinutesPerDayMax', blank=True,
                                                     null=True)  # Field name made lowercase.
    minutlunchbreakperdaymin = models.SmallIntegerField(db_column='MinutLunchBreakPerDayMin', blank=True,
                                                        null=True)  # Field name made lowercase.
    minutlunchbreakperdaymax = models.SmallIntegerField(db_column='MinutLunchBreakPerDayMax', blank=True,
                                                        null=True)  # Field name made lowercase.
    blocksnodays = models.SmallIntegerField(db_column='BlocksNoDays', blank=True,
                                            null=True)  # Field name made lowercase.
    blockslssnfrom = models.SmallIntegerField(db_column='BlocksLssnFrom', blank=True,
                                              null=True)  # Field name made lowercase.
    blockslssnto = models.SmallIntegerField(db_column='BlocksLssnTo', blank=True,
                                            null=True)  # Field name made lowercase.
    weekquotamin = models.SmallIntegerField(db_column='WeekQuotaMin', blank=True,
                                            null=True)  # Field name made lowercase.
    weekquotamax = models.SmallIntegerField(db_column='WeekQuotaMax', blank=True,
                                            null=True)  # Field name made lowercase.
    weekquotaideal = models.SmallIntegerField(db_column='WeekQuotaIdeal', blank=True,
                                              null=True)  # Field name made lowercase.
    nameyearbefore = models.CharField(db_column='NameYearBefore', max_length=20, blank=True,
                                      null=True)  # Field name made lowercase.
    periods_table_id = models.IntegerField(db_column='PERIODS_TABLE_ID', blank=True,
                                           null=True)  # Field name made lowercase.
    mainclass = models.CharField(db_column='MainClass', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    teacherids = models.CharField(db_column='TeacherIds', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID', blank=True, null=True)  # Field name made lowercase.
    department_id = models.IntegerField(db_column='DEPARTMENT_ID', blank=True, null=True)  # Field name made lowercase.
    ownschool = models.CharField(db_column='OwnSchool', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    msubjsuccmax = models.SmallIntegerField(db_column='MSubjSuccMax', blank=True,
                                            null=True)  # Field name made lowercase.
    msubjdaymax = models.SmallIntegerField(db_column='MSubjDayMax', blank=True, null=True)  # Field name made lowercase.
    classgroup = models.CharField(db_column='ClassGroup', max_length=1, blank=True,
                                  null=True)  # Field name made lowercase.
    classlevel = models.CharField(db_column='ClassLevel', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    nostudentmale = models.SmallIntegerField(db_column='NoStudentMale', blank=True,
                                             null=True)  # Field name made lowercase.
    nostudentfemale = models.SmallIntegerField(db_column='NoStudentFemale', blank=True,
                                               null=True)  # Field name made lowercase.
    minutmsubjdaymax = models.SmallIntegerField(db_column='MinutMSubjDayMax', blank=True,
                                                null=True)  # Field name made lowercase.
    minutbreakmax = models.SmallIntegerField(db_column='MinutBreakMax', blank=True,
                                             null=True)  # Field name made lowercase.
    notlastperiod = models.CharField(db_column='NotLastPeriod', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    doubleorsingle = models.CharField(db_column='DoubleOrSingle', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    substplgrid = models.CharField(db_column='SubstPlGrid', max_length=1000, blank=True,
                                   null=True)  # Field name made lowercase.
    nrtimegrid = models.SmallIntegerField(db_column='NrTimeGrid', blank=True, null=True)  # Field name made lowercase.
    difflessonmax = models.SmallIntegerField(db_column='DiffLessonMax', blank=True,
                                             null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plannedyear = models.IntegerField(db_column='PlannedYear', blank=True, null=True)  # Field name made lowercase.
    externname = models.CharField(db_column='ExternName', max_length=60, blank=True,
                                  null=True)  # Field name made lowercase.
    weeklytargetclasses = models.IntegerField(db_column='WeeklyTargetClasses', blank=True,
                                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Class'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'class_id', 'term_id'),)


class Commondata(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    id = models.SmallIntegerField(db_column='ID')  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner')  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    number1 = models.SmallIntegerField(db_column='Number1')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    fieldbool1 = models.IntegerField(db_column='FieldBool1', blank=True, null=True)  # Field name made lowercase.
    fieldbool2 = models.IntegerField(db_column='FieldBool2', blank=True, null=True)  # Field name made lowercase.
    fieldbool3 = models.IntegerField(db_column='FieldBool3', blank=True, null=True)  # Field name made lowercase.
    fieldbool4 = models.IntegerField(db_column='FieldBool4', blank=True, null=True)  # Field name made lowercase.
    fieldbool5 = models.IntegerField(db_column='FieldBool5', blank=True, null=True)  # Field name made lowercase.
    fieldbool6 = models.IntegerField(db_column='FieldBool6', blank=True, null=True)  # Field name made lowercase.
    fieldbool7 = models.IntegerField(db_column='FieldBool7', blank=True, null=True)  # Field name made lowercase.
    fieldbool8 = models.IntegerField(db_column='FieldBool8', blank=True, null=True)  # Field name made lowercase.
    fieldbyte1 = models.SmallIntegerField(db_column='FieldByte1', blank=True, null=True)  # Field name made lowercase.
    fieldbyte2 = models.SmallIntegerField(db_column='FieldByte2', blank=True, null=True)  # Field name made lowercase.
    fieldbyte3 = models.SmallIntegerField(db_column='FieldByte3', blank=True, null=True)  # Field name made lowercase.
    fieldbyte4 = models.SmallIntegerField(db_column='FieldByte4', blank=True, null=True)  # Field name made lowercase.
    fieldbyte5 = models.SmallIntegerField(db_column='FieldByte5', blank=True, null=True)  # Field name made lowercase.
    fieldbyte6 = models.SmallIntegerField(db_column='FieldByte6', blank=True, null=True)  # Field name made lowercase.
    fieldbyte7 = models.SmallIntegerField(db_column='FieldByte7', blank=True, null=True)  # Field name made lowercase.
    fieldbyte8 = models.SmallIntegerField(db_column='FieldByte8', blank=True, null=True)  # Field name made lowercase.
    fieldint1 = models.SmallIntegerField(db_column='FieldInt1', blank=True, null=True)  # Field name made lowercase.
    fieldint2 = models.SmallIntegerField(db_column='FieldInt2', blank=True, null=True)  # Field name made lowercase.
    fieldint3 = models.SmallIntegerField(db_column='FieldInt3', blank=True, null=True)  # Field name made lowercase.
    fieldint4 = models.SmallIntegerField(db_column='FieldInt4', blank=True, null=True)  # Field name made lowercase.
    fieldint5 = models.SmallIntegerField(db_column='FieldInt5', blank=True, null=True)  # Field name made lowercase.
    fieldint6 = models.SmallIntegerField(db_column='FieldInt6', blank=True, null=True)  # Field name made lowercase.
    fieldint7 = models.SmallIntegerField(db_column='FieldInt7', blank=True, null=True)  # Field name made lowercase.
    fieldint8 = models.SmallIntegerField(db_column='FieldInt8', blank=True, null=True)  # Field name made lowercase.
    fieldlong1 = models.IntegerField(db_column='FieldLong1', blank=True, null=True)  # Field name made lowercase.
    fieldlong2 = models.IntegerField(db_column='FieldLong2', blank=True, null=True)  # Field name made lowercase.
    fieldlong3 = models.IntegerField(db_column='FieldLong3', blank=True, null=True)  # Field name made lowercase.
    fieldlong4 = models.IntegerField(db_column='FieldLong4', blank=True, null=True)  # Field name made lowercase.
    fieldtext10a = models.CharField(db_column='FieldText10A', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext10b = models.CharField(db_column='FieldText10B', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext10c = models.CharField(db_column='FieldText10C', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext10d = models.CharField(db_column='FieldText10D', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext20a = models.CharField(db_column='FieldText20A', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext20b = models.CharField(db_column='FieldText20B', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext20c = models.CharField(db_column='FieldText20C', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext20d = models.CharField(db_column='FieldText20D', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext50a = models.CharField(db_column='FieldText50A', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext50b = models.CharField(db_column='FieldText50B', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext50c = models.CharField(db_column='FieldText50C', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext50d = models.CharField(db_column='FieldText50D', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    fieldtext100a = models.CharField(db_column='FieldText100A', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext100b = models.CharField(db_column='FieldText100B', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext100c = models.CharField(db_column='FieldText100C', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext100d = models.CharField(db_column='FieldText100D', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtextlonga = models.CharField(db_column='FieldTextLongA', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommonData'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'id', 'owner', 'number', 'number1'),)


class Corridor(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    corridor_id = models.IntegerField(db_column='CORRIDOR_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    dislocation = models.CharField(db_column='Dislocation', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    breaksupervision1 = models.CharField(db_column='BreakSupervision1', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision2 = models.CharField(db_column='BreakSupervision2', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision3 = models.CharField(db_column='BreakSupervision3', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision4 = models.CharField(db_column='BreakSupervision4', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision5 = models.CharField(db_column='BreakSupervision5', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision6 = models.CharField(db_column='BreakSupervision6', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision7 = models.CharField(db_column='BreakSupervision7', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision8 = models.CharField(db_column='BreakSupervision8', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision9 = models.CharField(db_column='BreakSupervision9', max_length=1000, blank=True,
                                         null=True)  # Field name made lowercase.
    breaksupervision10 = models.CharField(db_column='BreakSupervision10', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    breaksupervision11 = models.CharField(db_column='BreakSupervision11', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    breaksupervision12 = models.CharField(db_column='BreakSupervision12', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    breaksupervision13 = models.CharField(db_column='BreakSupervision13', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    breaksupervision14 = models.CharField(db_column='BreakSupervision14', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    breaksupervision15 = models.CharField(db_column='BreakSupervision15', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    breaksupervision16 = models.CharField(db_column='BreakSupervision16', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Corridor'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'corridor_id'),)


class Countvalue(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    count_value_id = models.IntegerField(db_column='COUNT_VALUE_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    lesson_id = models.IntegerField(db_column='LESSON_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    cv_reason_id = models.IntegerField(db_column='CV_REASON_ID', blank=True, null=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID', blank=True, null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    valueyear = models.IntegerField(db_column='ValueYear', blank=True, null=True)  # Field name made lowercase.
    percentvalue = models.SmallIntegerField(db_column='PercentValue', blank=True,
                                            null=True)  # Field name made lowercase.
    percentbase = models.CharField(db_column='PercentBase', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    valueweekminut = models.IntegerField(db_column='ValueWeekMinut', blank=True,
                                         null=True)  # Field name made lowercase.
    valueyearminut = models.IntegerField(db_column='ValueYearMinut', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CountValue'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'count_value_id'),)


class Couplcond(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    coupl_cond_id = models.IntegerField(db_column='COUPL_COND_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    conflict_coupl_cond_id = models.IntegerField(db_column='Conflict_COUPL_COND_ID', blank=True,
                                                 null=True)  # Field name made lowercase.
    maxcourses = models.SmallIntegerField(db_column='MaxCourses', blank=True, null=True)  # Field name made lowercase.
    lessonids = models.CharField(db_column='LessonIds', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    subjectids = models.CharField(db_column='SubjectIds', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CouplCond'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'coupl_cond_id'),)


class Department(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    department_id = models.IntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Department'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'department_id'),)


class Description(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Description'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'description_id'),)


class Event(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    event_id = models.IntegerField(db_column='EVENT_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    absence_reason_id = models.IntegerField(db_column='ABSENCE_REASON_ID', blank=True,
                                            null=True)  # Field name made lowercase.
    lessonfrom = models.SmallIntegerField(db_column='LessonFrom', blank=True, null=True)  # Field name made lowercase.
    lessonto = models.SmallIntegerField(db_column='LessonTo', blank=True, null=True)  # Field name made lowercase.
    eventelement1 = models.CharField(db_column='EventElement1', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement2 = models.CharField(db_column='EventElement2', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement3 = models.CharField(db_column='EventElement3', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement4 = models.CharField(db_column='EventElement4', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement5 = models.CharField(db_column='EventElement5', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement6 = models.CharField(db_column='EventElement6', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement7 = models.CharField(db_column='EventElement7', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement8 = models.CharField(db_column='EventElement8', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement9 = models.CharField(db_column='EventElement9', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    eventelement10 = models.CharField(db_column='EventElement10', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    timefrom = models.IntegerField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.IntegerField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.
    studentgroup = models.CharField(db_column='StudentGroup', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    studentgroup_id = models.IntegerField(db_column='STUDENTGROUP_ID', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Event'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'event_id'),)


class Exam(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    exam_id = models.IntegerField(db_column='EXAM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lessonfrom = models.SmallIntegerField(db_column='LessonFrom', blank=True, null=True)  # Field name made lowercase.
    lessonto = models.SmallIntegerField(db_column='LessonTo', blank=True, null=True)  # Field name made lowercase.
    examelement1 = models.CharField(db_column='ExamElement1', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement2 = models.CharField(db_column='ExamElement2', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement3 = models.CharField(db_column='ExamElement3', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement4 = models.CharField(db_column='ExamElement4', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement5 = models.CharField(db_column='ExamElement5', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement6 = models.CharField(db_column='ExamElement6', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement7 = models.CharField(db_column='ExamElement7', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement8 = models.CharField(db_column='ExamElement8', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement9 = models.CharField(db_column='ExamElement9', max_length=1000, blank=True,
                                    null=True)  # Field name made lowercase.
    examelement10 = models.CharField(db_column='ExamElement10', max_length=1000, blank=True,
                                     null=True)  # Field name made lowercase.
    substactive = models.IntegerField(db_column='SubstActive', blank=True, null=True)  # Field name made lowercase.
    noprintperiods = models.CharField(db_column='NoPrintPeriods', max_length=150, blank=True,
                                      null=True)  # Field name made lowercase.
    contrarytoabsence = models.CharField(db_column='ContraryToAbsence', max_length=150, blank=True,
                                         null=True)  # Field name made lowercase.
    messagesent = models.CharField(db_column='MessageSent', max_length=150, blank=True,
                                   null=True)  # Field name made lowercase.
    examperiodtexts = models.CharField(db_column='ExamPeriodTexts', max_length=2000, blank=True,
                                       null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exam'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'exam_id'),)


class Externelement(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    exel_id = models.IntegerField(db_column='EXEL_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    elementtype = models.SmallIntegerField(db_column='ElementType', blank=True, null=True)  # Field name made lowercase.
    ownerschool = models.IntegerField(db_column='OwnerSchool', blank=True, null=True)  # Field name made lowercase.
    allowedschools = models.CharField(db_column='AllowedSchools', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.
    lastchangedbyschool = models.IntegerField(db_column='LastChangedBySchool', blank=True,
                                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternElement'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'exel_id'),)


class Externindex(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    exel_id = models.IntegerField(db_column='EXEL_ID')  # Field name made lowercase.
    school_id1 = models.IntegerField(db_column='SCHOOL_ID1')  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='Year')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternIndex'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'exel_id', 'number', 'year', 'school_id1'),)


class Externtime(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    exel_id = models.IntegerField(db_column='EXEL_ID')  # Field name made lowercase.
    school_id1 = models.IntegerField(db_column='SCHOOL_ID1')  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='Year')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    weekday = models.SmallIntegerField(db_column='WeekDay', blank=True, null=True)  # Field name made lowercase.
    timefrom = models.SmallIntegerField(db_column='TimeFrom', blank=True, null=True)  # Field name made lowercase.
    timeto = models.SmallIntegerField(db_column='TimeTo', blank=True, null=True)  # Field name made lowercase.
    weeks = models.CharField(db_column='Weeks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    elements = models.CharField(db_column='Elements', max_length=1000, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternTime'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'number', 'exel_id', 'school_id1', 'year'),)


class Glaettung(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    weekfrom = models.SmallIntegerField(db_column='WeekFrom', blank=True, null=True)  # Field name made lowercase.
    weekto = models.SmallIntegerField(db_column='WeekTo', blank=True, null=True)  # Field name made lowercase.
    glaettung = models.IntegerField(db_column='Glaettung', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Glaettung'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'teacher_id', 'number'),)


class Holiday(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    holiday_id = models.IntegerField(db_column='HOLIDAY_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nextweek = models.SmallIntegerField(db_column='NextWeek', blank=True, null=True)  # Field name made lowercase.
    nextschoolweek = models.SmallIntegerField(db_column='NextSchoolWeek', blank=True,
                                              null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Holiday'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'holiday_id'),)


class Inputformat(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    input_format_id = models.IntegerField(db_column='INPUT_FORMAT_ID')  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    window = models.CharField(db_column='Window', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    miscdata = models.CharField(db_column='MiscData', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    picturedata1 = models.CharField(db_column='PictureData1', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    picturedata2 = models.CharField(db_column='PictureData2', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    font = models.CharField(db_column='Font', max_length=120, blank=True, null=True)  # Field name made lowercase.
    printer = models.CharField(db_column='Printer', max_length=60, blank=True, null=True)  # Field name made lowercase.
    printfont = models.CharField(db_column='PrintFont', max_length=120, blank=True,
                                 null=True)  # Field name made lowercase.
    actualelement_id2 = models.IntegerField(db_column='ActualELEMENT_ID2', blank=True,
                                            null=True)  # Field name made lowercase.
    headerfields = models.CharField(db_column='HeaderFields', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    type2 = models.SmallIntegerField(db_column='Type2', blank=True, null=True)  # Field name made lowercase.
    columnsstr = models.CharField(db_column='ColumnsStr', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    columnsactivestr = models.CharField(db_column='ColumnsActiveStr', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase.
    colwidthsstr = models.CharField(db_column='ColWidthsStr', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    layouthaeder = models.SmallIntegerField(db_column='LayoutHaeder', blank=True,
                                            null=True)  # Field name made lowercase.
    colsfixed = models.SmallIntegerField(db_column='ColsFixed', blank=True, null=True)  # Field name made lowercase.
    nocol = models.SmallIntegerField(db_column='NoCol', blank=True, null=True)  # Field name made lowercase.
    colwidth = models.SmallIntegerField(db_column='ColWidth', blank=True, null=True)  # Field name made lowercase.
    nocolteacher = models.SmallIntegerField(db_column='NoColTeacher', blank=True,
                                            null=True)  # Field name made lowercase.
    typex = models.CharField(db_column='TypeX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field6 = models.CharField(db_column='Field6', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field7 = models.CharField(db_column='Field7', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field8 = models.CharField(db_column='Field8', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field9 = models.CharField(db_column='Field9', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field10 = models.CharField(db_column='Field10', max_length=1000, blank=True,
                               null=True)  # Field name made lowercase.
    flags1 = models.CharField(db_column='Flags1', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InputFormat'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'input_format_id', 'owner'),)


class Lesson(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    lesson_id = models.IntegerField(db_column='LESSON_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=200, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    timerequest = models.CharField(db_column='TimeRequest', max_length=400, blank=True,
                                   null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    miscdata = models.CharField(db_column='MiscData', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    sortidfinper = models.SmallIntegerField(db_column='SortIdFinPer', blank=True,
                                            null=True)  # Field name made lowercase.
    lessonnr = models.IntegerField(db_column='LessonNr', blank=True, null=True)  # Field name made lowercase.
    periods = models.IntegerField(db_column='Periods', blank=True, null=True)  # Field name made lowercase.
    doublemin = models.IntegerField(db_column='DoubleMin', blank=True, null=True)  # Field name made lowercase.
    doublemax = models.IntegerField(db_column='DoubleMax', blank=True, null=True)  # Field name made lowercase.
    periodsroom = models.IntegerField(db_column='PeriodsRoom', blank=True, null=True)  # Field name made lowercase.
    periodsroommax = models.IntegerField(db_column='PeriodsRoomMax', blank=True,
                                         null=True)  # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    plannedyear = models.SmallIntegerField(db_column='PlannedYear', blank=True, null=True)  # Field name made lowercase.
    subjectseqcla = models.CharField(db_column='SubjectSeqCla', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    subjectseqtea = models.CharField(db_column='SubjectSeqTea', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    classcollision = models.CharField(db_column='ClassCollision', max_length=1, blank=True,
                                      null=True)  # Field name made lowercase.
    optflag = models.CharField(db_column='OptFlag', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lesngroups = models.CharField(db_column='LesnGroups', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    lessonelement1 = models.CharField(db_column='LessonElement1', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement2 = models.CharField(db_column='LessonElement2', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement3 = models.CharField(db_column='LessonElement3', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement4 = models.CharField(db_column='LessonElement4', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement5 = models.CharField(db_column='LessonElement5', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement6 = models.CharField(db_column='LessonElement6', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement7 = models.CharField(db_column='LessonElement7', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement8 = models.CharField(db_column='LessonElement8', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement9 = models.CharField(db_column='LessonElement9', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    lessonelement10 = models.CharField(db_column='LessonElement10', max_length=1000, blank=True,
                                       null=True)  # Field name made lowercase.
    lesson_tt = models.TextField(db_column='Lesson_TT', blank=True, null=True)  # Field name made lowercase.
    lesson_ttminut = models.TextField(db_column='Lesson_TTMinut', blank=True, null=True)  # Field name made lowercase.
    plannedweekminut = models.SmallIntegerField(db_column='PlannedWeekMinut', blank=True,
                                                null=True)  # Field name made lowercase.
    plannedyearminut = models.IntegerField(db_column='PlannedYearMinut', blank=True,
                                           null=True)  # Field name made lowercase.
    lesson_group_id = models.IntegerField(db_column='LESSON_GROUP_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    reasonnotplanned = models.SmallIntegerField(db_column='ReasonNotPlanned', blank=True,
                                                null=True)  # Field name made lowercase.
    timenotplanned = models.SmallIntegerField(db_column='TimeNotPlanned', blank=True,
                                              null=True)  # Field name made lowercase.
    block1 = models.SmallIntegerField(db_column='Block1', blank=True, null=True)  # Field name made lowercase.
    block2 = models.SmallIntegerField(db_column='Block2', blank=True, null=True)  # Field name made lowercase.
    block3 = models.SmallIntegerField(db_column='Block3', blank=True, null=True)  # Field name made lowercase.
    block4 = models.SmallIntegerField(db_column='Block4', blank=True, null=True)  # Field name made lowercase.
    block5 = models.SmallIntegerField(db_column='Block5', blank=True, null=True)  # Field name made lowercase.
    nostudentmin = models.SmallIntegerField(db_column='NoStudentMin', blank=True,
                                            null=True)  # Field name made lowercase.
    nostudentmax = models.SmallIntegerField(db_column='NoStudentMax', blank=True,
                                            null=True)  # Field name made lowercase.
    ypperperiod1 = models.CharField(db_column='YPPerPeriod1', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    ypperperiod2 = models.CharField(db_column='YPPerPeriod2', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    intensiveterm = models.CharField(db_column='IntensiveTerm', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    partnos = models.CharField(db_column='PartNos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    blockn = models.CharField(db_column='BlockN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isyearperiods = models.SmallIntegerField(db_column='IsYearPeriods', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lesson'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'lesson_id', 'term_id'),)


class Lessongroup(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    lesson_group_id = models.IntegerField(db_column='LESSON_GROUP_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID', blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    week = models.IntegerField(db_column='Week', blank=True, null=True)  # Field name made lowercase.
    inrerruptionsfrom = models.CharField(db_column='InrerruptionsFrom', max_length=255, blank=True,
                                         null=True)  # Field name made lowercase.
    inrerruptionsto = models.CharField(db_column='InrerruptionsTo', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    interruptionsfrom1 = models.CharField(db_column='InterruptionsFrom1', max_length=1000, blank=True,
                                          null=True)  # Field name made lowercase.
    interruptionsto1 = models.CharField(db_column='InterruptionsTo1', max_length=1000, blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LessonGroup'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'lesson_group_id'),)


class Lessonsequence(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    lesson_sequence_id = models.IntegerField(db_column='LESSON_SEQUENCE_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    periods = models.IntegerField(db_column='Periods', blank=True, null=True)  # Field name made lowercase.
    doubleperiods = models.IntegerField(db_column='DoublePeriods', blank=True, null=True)  # Field name made lowercase.
    lessonids = models.CharField(db_column='LessonIds', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LessonSequence'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'type', 'lesson_sequence_id', 'term_id'),)


class Lessonstack(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID')  # Field name made lowercase.
    stack_id = models.IntegerField(db_column='STACK_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    typestack = models.SmallIntegerField(db_column='TypeStack')  # Field name made lowercase.
    typeelement = models.SmallIntegerField(db_column='TypeElement')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    coordinates = models.CharField(db_column='Coordinates', max_length=2000, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LessonStack'
        unique_together = (
            ('school_id', 'schoolyear_id', 'version_id', 'user_id', 'stack_id', 'term_id', 'typestack', 'typeelement'),)


class Periodstable(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    periods_table_id = models.IntegerField(db_column='PERIODS_TABLE_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    pertabelement1 = models.CharField(db_column='PerTabElement1', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    pertabelement2 = models.CharField(db_column='PerTabElement2', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    pertabelement3 = models.CharField(db_column='PerTabElement3', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    pertabelement4 = models.CharField(db_column='PerTabElement4', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    pertabelement5 = models.CharField(db_column='PerTabElement5', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    pertabelement6 = models.CharField(db_column='PerTabElement6', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodsTable'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'periods_table_id'),)


class Prebooking(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    prebooking_id = models.IntegerField(db_column='PREBOOKING_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID', blank=True, null=True)  # Field name made lowercase.
    periods = models.SmallIntegerField(db_column='Periods', blank=True, null=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID', blank=True, null=True)  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    lesson_id = models.IntegerField(db_column='LESSON_ID', blank=True, null=True)  # Field name made lowercase.
    substitution_id = models.IntegerField(db_column='SUBSTITUTION_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    classids = models.CharField(db_column='ClassIds', max_length=1000, blank=True,
                                null=True)  # Field name made lowercase.
    studentids = models.CharField(db_column='StudentIds', max_length=1000, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prebooking'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'prebooking_id'),)


class Room(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timerequest = models.CharField(db_column='TimeRequest', max_length=400, blank=True,
                                   null=True)  # Field name made lowercase.
    timerequestminut = models.CharField(db_column='TimeRequestMinut', max_length=400, blank=True,
                                        null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    alternate_room_id = models.IntegerField(db_column='ALTERNATE_ROOM_ID', blank=True,
                                            null=True)  # Field name made lowercase.
    department_id = models.IntegerField(db_column='DEPARTMENT_ID', blank=True, null=True)  # Field name made lowercase.
    corridor1 = models.CharField(db_column='Corridor1', max_length=60, blank=True,
                                 null=True)  # Field name made lowercase.
    corridor2 = models.CharField(db_column='Corridor2', max_length=60, blank=True,
                                 null=True)  # Field name made lowercase.
    corridors = models.CharField(db_column='Corridors', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    dislocation = models.CharField(db_column='Dislocation', max_length=1, blank=True,
                                   null=True)  # Field name made lowercase.
    capacity = models.SmallIntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    weighting = models.SmallIntegerField(db_column='Weighting', blank=True, null=True)  # Field name made lowercase.
    minutbreakmin = models.SmallIntegerField(db_column='MinutBreakMin', blank=True,
                                             null=True)  # Field name made lowercase.
    externname = models.CharField(db_column='ExternName', max_length=60, blank=True,
                                  null=True)  # Field name made lowercase.
    departments = models.CharField(db_column='Departments', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Room'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'room_id', 'term_id'),)


class Roomgroup(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    roomgroup_id = models.IntegerField(db_column='ROOMGROUP_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    roomids = models.CharField(db_column='RoomIds', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomGroup'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'roomgroup_id'),)


class School(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolno = models.CharField(db_column='SchoolNo', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    lizense1 = models.CharField(db_column='Lizense1', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    lizense2 = models.CharField(db_column='Lizense2', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    lizensenr1 = models.CharField(db_column='LizenseNr1', max_length=8, blank=True,
                                  null=True)  # Field name made lowercase.
    lizensenr2 = models.CharField(db_column='LizenseNr2', max_length=7, blank=True,
                                  null=True)  # Field name made lowercase.
    lizensenr3 = models.CharField(db_column='LizenseNr3', max_length=7, blank=True,
                                  null=True)  # Field name made lowercase.
    expirationdate = models.IntegerField(db_column='ExpirationDate', blank=True,
                                         null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.SmallIntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID', blank=True, null=True)  # Field name made lowercase.
    lightmodus = models.IntegerField(db_column='LightModus', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numberstudents = models.IntegerField(db_column='NumberStudents', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'School'


class Schoolyear(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    counterlast = models.IntegerField(db_column='CounterLast', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    schoolyearzoned = models.CharField(db_column='SchoolYearZoned', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SchoolYear'
        unique_together = (('school_id', 'schoolyear_id'),)


class Screenset(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    screenset_id = models.IntegerField(db_column='SCREENSET_ID')  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    modus = models.CharField(db_column='Modus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numbers = models.SmallIntegerField(db_column='NumberS', blank=True, null=True)  # Field name made lowercase.
    windows1 = models.CharField(db_column='Windows1', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    windows2 = models.CharField(db_column='Windows2', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    windows3 = models.CharField(db_column='Windows3', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    windows4 = models.CharField(db_column='Windows4', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    windows5 = models.CharField(db_column='Windows5', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    windows6 = models.CharField(db_column='Windows6', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ScreenSet'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'screenset_id', 'owner'),)


class Student(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    student_id = models.IntegerField(db_column='STUDENT_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=150, blank=True,
                                 null=True)  # Field name made lowercase.
    studnumber = models.CharField(db_column='StudNumber', max_length=20, blank=True,
                                  null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.IntegerField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    optsign = models.CharField(db_column='OptSign', max_length=1, blank=True, null=True)  # Field name made lowercase.
    class_id = models.IntegerField(db_column='CLASS_ID', blank=True, null=True)  # Field name made lowercase.
    class_id2 = models.SmallIntegerField(db_column='CLASS_ID2', blank=True, null=True)  # Field name made lowercase.
    class_id3 = models.SmallIntegerField(db_column='CLASS_ID3', blank=True, null=True)  # Field name made lowercase.
    class_id4 = models.SmallIntegerField(db_column='CLASS_ID4', blank=True, null=True)  # Field name made lowercase.
    class_id5 = models.SmallIntegerField(db_column='CLASS_ID5', blank=True, null=True)  # Field name made lowercase.
    class_id6 = models.SmallIntegerField(db_column='CLASS_ID6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'student_id'),)


class Studentchoice(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    student_id = models.IntegerField(db_column='STUDENT_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberalternativegiven = models.SmallIntegerField(db_column='NumberAlternativeGiven', blank=True,
                                                      null=True)  # Field name made lowercase.
    alternativecourses = models.CharField(db_column='AlternativeCourses', max_length=255, blank=True,
                                          null=True)  # Field name made lowercase.
    standbycourses = models.CharField(db_column='StandByCourses', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentChoice'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'student_id', 'term_id', 'number'),)


class Studentgroup(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    studentgroup_id = models.IntegerField(db_column='STUDENTGROUP_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='SUBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    classids = models.CharField(db_column='ClassIds', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentGroup'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'studentgroup_id'),)


class Subjectgroup(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    subjectgroup_id = models.IntegerField(db_column='SUBJECTGROUP_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    subjectids = models.CharField(db_column='SubjectIds', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubjectGroup'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'subjectgroup_id'),)


class Subjects(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    subject_id = models.IntegerField(db_column='SUBJECT_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timerequest = models.CharField(db_column='TimeRequest', max_length=400, blank=True,
                                   null=True)  # Field name made lowercase.
    timerequestminut = models.CharField(db_column='TimeRequestMinut', max_length=400, blank=True,
                                        null=True)  # Field name made lowercase.
    selmatrix = models.CharField(db_column='SelMatrix', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID', blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    miscdata = models.CharField(db_column='MiscData', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    sujectgroup = models.CharField(db_column='SujectGroup', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    subjectseqcla = models.CharField(db_column='SubjectSeqCla', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    subjectseqtea = models.CharField(db_column='SubjectSeqTea', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    lssnpmmin = models.SmallIntegerField(db_column='LssnPMmin', blank=True, null=True)  # Field name made lowercase.
    lssnpmmax = models.SmallIntegerField(db_column='LssnPMmax', blank=True, null=True)  # Field name made lowercase.
    lssnweekmin = models.SmallIntegerField(db_column='LssnWeekMin', blank=True, null=True)  # Field name made lowercase.
    lssnweekmax = models.SmallIntegerField(db_column='LssnWeekMax', blank=True, null=True)  # Field name made lowercase.
    minutpmmin = models.SmallIntegerField(db_column='MinutPMmin', blank=True, null=True)  # Field name made lowercase.
    minutpmmax = models.SmallIntegerField(db_column='MinutPMmax', blank=True, null=True)  # Field name made lowercase.
    minutbreak1 = models.SmallIntegerField(db_column='MinutBreak1', blank=True, null=True)  # Field name made lowercase.
    minutbreak2 = models.SmallIntegerField(db_column='MinutBreak2', blank=True, null=True)  # Field name made lowercase.
    minutlssn = models.SmallIntegerField(db_column='MinutLssn', blank=True, null=True)  # Field name made lowercase.
    minutlssnweekmin = models.SmallIntegerField(db_column='MinutLssnWeekMin', blank=True,
                                                null=True)  # Field name made lowercase.
    minutlssnweekmax = models.SmallIntegerField(db_column='MinutLssnWeekMax', blank=True,
                                                null=True)  # Field name made lowercase.
    departments = models.CharField(db_column='Departments', max_length=120, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subjects'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'subject_id'),)


class Substitution(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    substitution_id = models.IntegerField(db_column='SUBSTITUTION_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    lesson = models.SmallIntegerField(db_column='Lesson', blank=True, null=True)  # Field name made lowercase.
    teacher_idsubst = models.IntegerField(db_column='TEACHER_IDSubst', blank=True,
                                          null=True)  # Field name made lowercase.
    teacher_idlessn = models.IntegerField(db_column='TEACHER_IDLessn', blank=True,
                                          null=True)  # Field name made lowercase.
    subject_idsubst = models.IntegerField(db_column='SUBJECT_IDSubst', blank=True,
                                          null=True)  # Field name made lowercase.
    room_idsubst = models.IntegerField(db_column='ROOM_IDSubst', blank=True, null=True)  # Field name made lowercase.
    lesson_idsubst = models.IntegerField(db_column='LESSON_IDSubst', blank=True,
                                         null=True)  # Field name made lowercase.
    corridor_id = models.IntegerField(db_column='CORRIDOR_ID', blank=True, null=True)  # Field name made lowercase.
    transfer_id = models.IntegerField(db_column='TRANSFER_ID', blank=True, null=True)  # Field name made lowercase.
    exam_id = models.IntegerField(db_column='EXAM_ID', blank=True, null=True)  # Field name made lowercase.
    caused_by_exam_id = models.IntegerField(db_column='CAUSED_BY_EXAM_ID', blank=True,
                                            null=True)  # Field name made lowercase.
    coupling = models.SmallIntegerField(db_column='Coupling', blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    classids = models.CharField(db_column='ClassIds', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    absenceids = models.CharField(db_column='AbsenceIds', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    prebookingnr = models.IntegerField(db_column='PrebookingNr', blank=True, null=True)  # Field name made lowercase.
    prebookingnrtransfer = models.IntegerField(db_column='PrebookingNrTransfer', blank=True,
                                               null=True)  # Field name made lowercase.
    studentids = models.CharField(db_column='StudentIds', max_length=1000, blank=True,
                                  null=True)  # Field name made lowercase.
    substvalue = models.CharField(db_column='SubstValue', max_length=9, blank=True,
                                  null=True)  # Field name made lowercase.
    studentgroup = models.CharField(db_column='StudentGroup', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    roomids = models.CharField(db_column='RoomIds', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookingtype = models.IntegerField(db_column='BookingType', blank=True, null=True)  # Field name made lowercase.
    studentgroup_id = models.IntegerField(db_column='STUDENTGROUP_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    breaksubstdata = models.CharField(db_column='BreakSubstData', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Substitution'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'substitution_id'),)


class Ttelementfilter(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    tt_element_filter_id = models.IntegerField(db_column='TT_ELEMENT_FILTER_ID')  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    elementids = models.CharField(db_column='ElementIds', max_length=1000, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TTElementFilter'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'tt_element_filter_id', 'owner'),)


class TtFormat(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    tt_format_id = models.IntegerField(db_column='TT_FORMAT_ID')  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    window = models.CharField(db_column='Window', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    picturedata1 = models.CharField(db_column='PictureData1', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    picturedata2 = models.CharField(db_column='PictureData2', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    font = models.CharField(db_column='Font', max_length=120, blank=True, null=True)  # Field name made lowercase.
    printer = models.CharField(db_column='Printer', max_length=60, blank=True, null=True)  # Field name made lowercase.
    header11 = models.SmallIntegerField(db_column='Header11', blank=True, null=True)  # Field name made lowercase.
    headerweek = models.SmallIntegerField(db_column='HeaderWeek', blank=True, null=True)  # Field name made lowercase.
    typeheader1 = models.SmallIntegerField(db_column='TypeHeader1', blank=True, null=True)  # Field name made lowercase.
    typeheader2 = models.SmallIntegerField(db_column='TypeHeader2', blank=True, null=True)  # Field name made lowercase.
    format = models.SmallIntegerField(db_column='Format', blank=True, null=True)  # Field name made lowercase.
    fixedflag = models.SmallIntegerField(db_column='FixedFlag', blank=True, null=True)  # Field name made lowercase.
    nocol = models.SmallIntegerField(db_column='NoCol', blank=True, null=True)  # Field name made lowercase.
    col1 = models.SmallIntegerField(db_column='Col1', blank=True, null=True)  # Field name made lowercase.
    colact = models.SmallIntegerField(db_column='ColAct', blank=True, null=True)  # Field name made lowercase.
    nocol11 = models.SmallIntegerField(db_column='NoCol11', blank=True, null=True)  # Field name made lowercase.
    nocol20_30 = models.SmallIntegerField(db_column='NoCol20_30', blank=True, null=True)  # Field name made lowercase.
    nocolftn = models.SmallIntegerField(db_column='NoColFtn', blank=True, null=True)  # Field name made lowercase.
    nocolftn11_30 = models.SmallIntegerField(db_column='NoColFtn11_30', blank=True,
                                             null=True)  # Field name made lowercase.
    cola = models.SmallIntegerField(db_column='ColA', blank=True, null=True)  # Field name made lowercase.
    norow = models.SmallIntegerField(db_column='NoRow', blank=True, null=True)  # Field name made lowercase.
    row1 = models.SmallIntegerField(db_column='Row1', blank=True, null=True)  # Field name made lowercase.
    rowact = models.SmallIntegerField(db_column='RowAct', blank=True, null=True)  # Field name made lowercase.
    norow11 = models.SmallIntegerField(db_column='NoRow11', blank=True, null=True)  # Field name made lowercase.
    norow20_30 = models.SmallIntegerField(db_column='NoRow20_30', blank=True, null=True)  # Field name made lowercase.
    norowtitle = models.SmallIntegerField(db_column='NoRowTitle', blank=True, null=True)  # Field name made lowercase.
    rowa = models.SmallIntegerField(db_column='RowA', blank=True, null=True)  # Field name made lowercase.
    typetitle = models.SmallIntegerField(db_column='TypeTitle', blank=True, null=True)  # Field name made lowercase.
    intheadingrow11_30 = models.SmallIntegerField(db_column='IntHeadingRow11_30', blank=True,
                                                  null=True)  # Field name made lowercase.
    elperpage40 = models.SmallIntegerField(db_column='ElPerPage40', blank=True, null=True)  # Field name made lowercase.
    intheadingcol11_30 = models.SmallIntegerField(db_column='IntHeadingCol11_30', blank=True,
                                                  null=True)  # Field name made lowercase.
    tt_version = models.SmallIntegerField(db_column='TT_Version', blank=True, null=True)  # Field name made lowercase.
    nodayspersheet = models.SmallIntegerField(db_column='NoDaysPerSheet', blank=True,
                                              null=True)  # Field name made lowercase.
    layoutheader = models.SmallIntegerField(db_column='LayoutHeader', blank=True,
                                            null=True)  # Field name made lowercase.
    layoutlessn = models.SmallIntegerField(db_column='LayoutLessn', blank=True, null=True)  # Field name made lowercase.
    layoutlessn1 = models.SmallIntegerField(db_column='LayoutLessn1', blank=True,
                                            null=True)  # Field name made lowercase.
    position1 = models.SmallIntegerField(db_column='Position1', blank=True, null=True)  # Field name made lowercase.
    position2 = models.SmallIntegerField(db_column='Position2', blank=True, null=True)  # Field name made lowercase.
    position3 = models.SmallIntegerField(db_column='Position3', blank=True, null=True)  # Field name made lowercase.
    nottperpage = models.SmallIntegerField(db_column='NoTTPerPage', blank=True, null=True)  # Field name made lowercase.
    nottperpage1 = models.SmallIntegerField(db_column='NoTTPerPage1', blank=True,
                                            null=True)  # Field name made lowercase.
    nottperpage2 = models.SmallIntegerField(db_column='NoTTPerPage2', blank=True,
                                            null=True)  # Field name made lowercase.
    periodfrom = models.SmallIntegerField(db_column='PeriodFrom', blank=True, null=True)  # Field name made lowercase.
    periodto = models.SmallIntegerField(db_column='PeriodTo', blank=True, null=True)  # Field name made lowercase.
    weekperiodfrom = models.SmallIntegerField(db_column='WeekPeriodFrom', blank=True,
                                              null=True)  # Field name made lowercase.
    weekperiodto = models.SmallIntegerField(db_column='WeekPeriodTo', blank=True,
                                            null=True)  # Field name made lowercase.
    nonamesperline = models.SmallIntegerField(db_column='NoNamesPerLine', blank=True,
                                              null=True)  # Field name made lowercase.
    notimesperline = models.SmallIntegerField(db_column='NoTimesPerLine', blank=True,
                                              null=True)  # Field name made lowercase.
    minutdayfrom = models.SmallIntegerField(db_column='MinutDayFrom', blank=True,
                                            null=True)  # Field name made lowercase.
    minutdayto = models.SmallIntegerField(db_column='MinutDayTo', blank=True, null=True)  # Field name made lowercase.
    minutperiodfrom = models.SmallIntegerField(db_column='MinutPeriodFrom', blank=True,
                                               null=True)  # Field name made lowercase.
    minutperiodto = models.SmallIntegerField(db_column='MinutPeriodTo', blank=True,
                                             null=True)  # Field name made lowercase.
    minutweekperiodfrom = models.SmallIntegerField(db_column='MinutWeekPeriodFrom', blank=True,
                                                   null=True)  # Field name made lowercase.
    minutweekperiodto = models.SmallIntegerField(db_column='MinutWeekPeriodTo', blank=True,
                                                 null=True)  # Field name made lowercase.
    input_format_id = models.IntegerField(db_column='INPUT_FORMAT_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    sizeleftx = models.SmallIntegerField(db_column='SizeLeftX', blank=True, null=True)  # Field name made lowercase.
    sizelefty = models.SmallIntegerField(db_column='SizeLeftY', blank=True, null=True)  # Field name made lowercase.
    sizetopx = models.SmallIntegerField(db_column='SizeTopX', blank=True, null=True)  # Field name made lowercase.
    sizetopy = models.SmallIntegerField(db_column='SizeTopY', blank=True, null=True)  # Field name made lowercase.
    htmltitlewidth = models.SmallIntegerField(db_column='HtmlTitleWidth', blank=True,
                                              null=True)  # Field name made lowercase.
    htmlcolheight = models.SmallIntegerField(db_column='HtmlColHeight', blank=True,
                                             null=True)  # Field name made lowercase.
    htmlcolwidth = models.SmallIntegerField(db_column='HtmlColWidth', blank=True,
                                            null=True)  # Field name made lowercase.
    htmltitlealign = models.SmallIntegerField(db_column='HtmlTitleAlign', blank=True,
                                              null=True)  # Field name made lowercase.
    htmlcolalign = models.SmallIntegerField(db_column='HtmlColAlign', blank=True,
                                            null=True)  # Field name made lowercase.
    htmlfieldwidth = models.SmallIntegerField(db_column='HtmlFieldWidth', blank=True,
                                              null=True)  # Field name made lowercase.
    relativefont1 = models.CharField(db_column='RelativeFont1', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont2 = models.CharField(db_column='RelativeFont2', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont3 = models.CharField(db_column='RelativeFont3', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont4 = models.CharField(db_column='RelativeFont4', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont5 = models.CharField(db_column='RelativeFont5', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont6 = models.CharField(db_column='RelativeFont6', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont7 = models.CharField(db_column='RelativeFont7', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont8 = models.CharField(db_column='RelativeFont8', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont9 = models.CharField(db_column='RelativeFont9', max_length=60, blank=True,
                                     null=True)  # Field name made lowercase.
    relativefont10 = models.CharField(db_column='RelativeFont10', max_length=60, blank=True,
                                      null=True)  # Field name made lowercase.
    relativefont11 = models.CharField(db_column='RelativeFont11', max_length=60, blank=True,
                                      null=True)  # Field name made lowercase.
    relativefont12 = models.CharField(db_column='RelativeFont12', max_length=60, blank=True,
                                      null=True)  # Field name made lowercase.
    relativefont13 = models.CharField(db_column='RelativeFont13', max_length=60, blank=True,
                                      null=True)  # Field name made lowercase.
    relativefont14 = models.CharField(db_column='RelativeFont14', max_length=60, blank=True,
                                      null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field2 = models.CharField(db_column='Field2', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field4 = models.CharField(db_column='Field4', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field5 = models.CharField(db_column='Field5', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field6 = models.CharField(db_column='Field6', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field7 = models.CharField(db_column='Field7', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field8 = models.CharField(db_column='Field8', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field9 = models.CharField(db_column='Field9', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    field10 = models.CharField(db_column='Field10', max_length=1000, blank=True,
                               null=True)  # Field name made lowercase.
    linesforheader = models.CharField(db_column='LinesForHeader', max_length=200, blank=True,
                                      null=True)  # Field name made lowercase.
    schoolweeks = models.CharField(db_column='SchoolWeeks', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    flags1 = models.CharField(db_column='Flags1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    noweeks = models.SmallIntegerField(db_column='NoWeeks', blank=True, null=True)  # Field name made lowercase.
    nott = models.IntegerField(db_column='NoTT', blank=True, null=True)  # Field name made lowercase.
    showlines = models.CharField(db_column='ShowLines', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    doublelines = models.CharField(db_column='DoubleLines', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    thicklines = models.CharField(db_column='ThickLines', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    additionalheader = models.CharField(db_column='AdditionalHeader', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase.
    positionclateasub = models.SmallIntegerField(db_column='PositionClaTeaSub', blank=True,
                                                 null=True)  # Field name made lowercase.
    colclateasub = models.SmallIntegerField(db_column='ColClaTeaSub', blank=True,
                                            null=True)  # Field name made lowercase.
    colclateasub_subperline = models.SmallIntegerField(db_column='ColClaTeaSub_SubPerLine', blank=True,
                                                       null=True)  # Field name made lowercase.
    positionadditionaltt = models.SmallIntegerField(db_column='PositionAdditionalTT', blank=True,
                                                    null=True)  # Field name made lowercase.
    nameadditionaltt = models.CharField(db_column='NameAdditionalTT', max_length=60, blank=True,
                                        null=True)  # Field name made lowercase.
    flags2 = models.CharField(db_column='Flags2', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TT_Format'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'tt_format_id', 'owner'),)


class Tableinfo(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.SmallIntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    idmax = models.IntegerField(db_column='IdMax', blank=True, null=True)  # Field name made lowercase.
    sortidmax = models.IntegerField(db_column='SortIdMax', blank=True, null=True)  # Field name made lowercase.
    lessonnrmax = models.IntegerField(db_column='LessonNrMax', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableInfo'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'type', 'id'),)


class Teacher(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID')  # Field name made lowercase.
    term_id = models.SmallIntegerField(db_column='TERM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    statisticcodes = models.CharField(db_column='StatisticCodes', max_length=10, blank=True,
                                      null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timerequest = models.CharField(db_column='TimeRequest', max_length=400, blank=True,
                                   null=True)  # Field name made lowercase.
    timerequestminut = models.CharField(db_column='TimeRequestMinut', max_length=400, blank=True,
                                        null=True)  # Field name made lowercase.
    dayrequest = models.CharField(db_column='DayRequest', max_length=400, blank=True,
                                  null=True)  # Field name made lowercase.
    timerequestunspecified = models.CharField(db_column='TimeRequestUnspecified', max_length=400, blank=True,
                                              null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=400, blank=True, null=True)  # Field name made lowercase.
    selmatrix = models.CharField(db_column='SelMatrix', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    blankflags = models.CharField(db_column='BlankFlags', max_length=80, blank=True,
                                  null=True)  # Field name made lowercase.
    room_id = models.IntegerField(db_column='ROOM_ID', blank=True, null=True)  # Field name made lowercase.
    description_id = models.IntegerField(db_column='DESCRIPTION_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    factor = models.CharField(db_column='Factor', max_length=9, blank=True, null=True)  # Field name made lowercase.
    foreigndata = models.CharField(db_column='ForeignData', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    foreignkey = models.CharField(db_column='ForeignKey', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    miscdata = models.CharField(db_column='MiscData', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=60, blank=True, null=True)  # Field name made lowercase.
    minutbreakmin = models.SmallIntegerField(db_column='MinutBreakMin', blank=True,
                                             null=True)  # Field name made lowercase.
    lunchbreakmin = models.SmallIntegerField(db_column='LunchBreakMin', blank=True,
                                             null=True)  # Field name made lowercase.
    lunchbreakmax = models.SmallIntegerField(db_column='LunchBreakMax', blank=True,
                                             null=True)  # Field name made lowercase.
    lssnperdaymin = models.SmallIntegerField(db_column='LssnPerDayMin', blank=True,
                                             null=True)  # Field name made lowercase.
    lssnperdaymax = models.SmallIntegerField(db_column='LssnPerDayMax', blank=True,
                                             null=True)  # Field name made lowercase.
    minutminutesperdaymin = models.SmallIntegerField(db_column='MinutMinutesPerDayMin', blank=True,
                                                     null=True)  # Field name made lowercase.
    minutminutesperdaymax = models.SmallIntegerField(db_column='MinutMinutesPerDayMax', blank=True,
                                                     null=True)  # Field name made lowercase.
    minutlunchbreakperdaymin = models.SmallIntegerField(db_column='MinutLunchBreakPerDayMin', blank=True,
                                                        null=True)  # Field name made lowercase.
    minutlunchbreakperdaymax = models.SmallIntegerField(db_column='MinutLunchBreakPerDayMax', blank=True,
                                                        null=True)  # Field name made lowercase.
    blocksnodays = models.SmallIntegerField(db_column='BlocksNoDays', blank=True,
                                            null=True)  # Field name made lowercase.
    blockslssnfrom = models.SmallIntegerField(db_column='BlocksLssnFrom', blank=True,
                                              null=True)  # Field name made lowercase.
    blockslssnto = models.SmallIntegerField(db_column='BlocksLssnTo', blank=True,
                                            null=True)  # Field name made lowercase.
    weekquotamin = models.SmallIntegerField(db_column='WeekQuotaMin', blank=True,
                                            null=True)  # Field name made lowercase.
    weekquotamax = models.SmallIntegerField(db_column='WeekQuotaMax', blank=True,
                                            null=True)  # Field name made lowercase.
    weekquotaideal = models.SmallIntegerField(db_column='WeekQuotaIdeal', blank=True,
                                              null=True)  # Field name made lowercase.
    pnumber = models.CharField(db_column='PNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=150, blank=True,
                                 null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ownschool = models.CharField(db_column='OwnSchool', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    ignorereason = models.CharField(db_column='IgnoreReason', max_length=20, blank=True,
                                    null=True)  # Field name made lowercase.
    department_id1 = models.SmallIntegerField(db_column='DEPARTMENT_ID1', blank=True,
                                              null=True)  # Field name made lowercase.
    department_id2 = models.SmallIntegerField(db_column='DEPARTMENT_ID2', blank=True,
                                              null=True)  # Field name made lowercase.
    department_id3 = models.SmallIntegerField(db_column='DEPARTMENT_ID3', blank=True,
                                              null=True)  # Field name made lowercase.
    department_id4 = models.SmallIntegerField(db_column='DEPARTMENT_ID4', blank=True,
                                              null=True)  # Field name made lowercase.
    department_id5 = models.SmallIntegerField(db_column='DEPARTMENT_ID5', blank=True,
                                              null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    handy = models.CharField(db_column='Handy', max_length=20, blank=True, null=True)  # Field name made lowercase.
    externid = models.CharField(db_column='ExternId', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    nolessnsucc = models.SmallIntegerField(db_column='NoLessnSucc', blank=True, null=True)  # Field name made lowercase.
    cavitymin = models.SmallIntegerField(db_column='CavityMin', blank=True, null=True)  # Field name made lowercase.
    cavitymax = models.SmallIntegerField(db_column='CavityMax', blank=True, null=True)  # Field name made lowercase.
    availmax = models.SmallIntegerField(db_column='AvailMax', blank=True, null=True)  # Field name made lowercase.
    daybreak = models.SmallIntegerField(db_column='DayBreak', blank=True, null=True)  # Field name made lowercase.
    substblock = models.SmallIntegerField(db_column='SubstBlock', blank=True, null=True)  # Field name made lowercase.
    minutbreaksweekmin = models.SmallIntegerField(db_column='MinutBreaksWeekMin', blank=True,
                                                  null=True)  # Field name made lowercase.
    minutbreaksweekmax = models.SmallIntegerField(db_column='MinutBreaksWeekMax', blank=True,
                                                  null=True)  # Field name made lowercase.
    minutsucessmax = models.SmallIntegerField(db_column='MinutSucessMax', blank=True,
                                              null=True)  # Field name made lowercase.
    pointbreaksupmax = models.SmallIntegerField(db_column='PointBreaksupMax', blank=True,
                                                null=True)  # Field name made lowercase.
    birthdate = models.IntegerField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.IntegerField(db_column='ArrivalDate', blank=True, null=True)  # Field name made lowercase.
    departuredate = models.IntegerField(db_column='DepartureDate', blank=True, null=True)  # Field name made lowercase.
    plannedweek = models.IntegerField(db_column='PlannedWeek', blank=True, null=True)  # Field name made lowercase.
    plannedweekmax = models.IntegerField(db_column='PlannedWeekMax', blank=True,
                                         null=True)  # Field name made lowercase.
    plannedyear = models.IntegerField(db_column='PlannedYear', blank=True, null=True)  # Field name made lowercase.
    plannedyearmax = models.IntegerField(db_column='PlannedYearMax', blank=True,
                                         null=True)  # Field name made lowercase.
    salarypehour = models.IntegerField(db_column='SalaryPeHour', blank=True, null=True)  # Field name made lowercase.
    optvarteacher = models.CharField(db_column='OptVarTeacher', max_length=1, blank=True,
                                     null=True)  # Field name made lowercase.
    externname = models.CharField(db_column='ExternName', max_length=60, blank=True,
                                  null=True)  # Field name made lowercase.
    breaksvrequest = models.CharField(db_column='BreakSVRequest', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    teachquali1 = models.CharField(db_column='TeachQuali1', max_length=1000, blank=True,
                                   null=True)  # Field name made lowercase.
    teachquali2 = models.CharField(db_column='TeachQuali2', max_length=1000, blank=True,
                                   null=True)  # Field name made lowercase.
    teachquali3 = models.CharField(db_column='TeachQuali3', max_length=1000, blank=True,
                                   null=True)  # Field name made lowercase.
    teachquali4 = models.CharField(db_column='TeachQuali4', max_length=1000, blank=True,
                                   null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='Text2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    glaettdate = models.IntegerField(db_column='GlaettDate', blank=True, null=True)  # Field name made lowercase.
    breaksvdayflags = models.CharField(db_column='BreakSvDayFlags', max_length=100, blank=True,
                                       null=True)  # Field name made lowercase.
    lengthstaymax = models.SmallIntegerField(db_column='LengthStayMax', blank=True,
                                             null=True)  # Field name made lowercase.
    statusnew = models.CharField(db_column='StatusNew', max_length=10, blank=True,
                                 null=True)  # Field name made lowercase.
    statusnewdate = models.IntegerField(db_column='StatusNewDate', blank=True, null=True)  # Field name made lowercase.
    text3 = models.CharField(db_column='Text3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    text4 = models.CharField(db_column='Text4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plannedweekminut = models.IntegerField(db_column='PlannedWeekMinut', blank=True,
                                           null=True)  # Field name made lowercase.
    plannedyearminut = models.IntegerField(db_column='PlannedYearMinut', blank=True,
                                           null=True)  # Field name made lowercase.
    plannedweeknew = models.IntegerField(db_column='PlannedWeekNew', blank=True,
                                         null=True)  # Field name made lowercase.
    plannedperdept = models.CharField(db_column='PlannedPerDept', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teacher'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'teacher_id', 'term_id'),)


class Teachergroup(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    teachergroup_id = models.IntegerField(db_column='TEACHERGROUP_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    forecolor = models.IntegerField(db_column='ForeColor', blank=True, null=True)  # Field name made lowercase.
    backcolor = models.IntegerField(db_column='BackColor', blank=True, null=True)  # Field name made lowercase.
    teacherids = models.CharField(db_column='TeacherIds', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    dataperteacher = models.CharField(db_column='DataPerTeacher', max_length=255, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TeacherGroup'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'teachergroup_id'),)


class Terms(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    term_id = models.IntegerField(db_column='TERM_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='Longname', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    term_id_mother = models.IntegerField(db_column='TERM_ID_Mother', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Terms'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'term_id'),)


class Transfer(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    transfer_id = models.IntegerField(db_column='TRANSFER_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID', blank=True, null=True)  # Field name made lowercase.
    lesson_id = models.IntegerField(db_column='LESSON_ID', blank=True, null=True)  # Field name made lowercase.
    datefrom = models.IntegerField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.IntegerField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    lessonfrom = models.SmallIntegerField(db_column='LessonFrom', blank=True, null=True)  # Field name made lowercase.
    lessonto = models.SmallIntegerField(db_column='LessonTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transfer'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'transfer_id'),)


class Untissettings(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    option_id = models.IntegerField(db_column='OPTION_ID')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner', blank=True, null=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=1000, blank=True,
                               null=True)  # Field name made lowercase.
    optionkey = models.CharField(db_column='OptionKey', max_length=1000, blank=True,
                                 null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UntisSettings'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'option_id'),)


class User(models.Model, PureDjangoModel):
    user_id = models.SmallIntegerField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    user_group_id = models.SmallIntegerField(db_column='USER_GROUP_ID', blank=True,
                                             null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_id2 = models.SmallIntegerField(db_column='USER_ID2', blank=True, null=True)  # Field name made lowercase.
    user2text = models.CharField(db_column='User2Text', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    password = models.IntegerField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    loggedin = models.IntegerField(db_column='LoggedIn', blank=True, null=True)  # Field name made lowercase.
    usercounterlast = models.IntegerField(db_column='UserCounterLast', blank=True,
                                          null=True)  # Field name made lowercase.
    logindate = models.IntegerField(db_column='LogInDate', blank=True, null=True)  # Field name made lowercase.
    logintime = models.SmallIntegerField(db_column='LogInTime', blank=True, null=True)  # Field name made lowercase.
    logoutdate = models.IntegerField(db_column='LogOutDate', blank=True, null=True)  # Field name made lowercase.
    logouttime = models.SmallIntegerField(db_column='LogOutTime', blank=True, null=True)  # Field name made lowercase.
    refreshdate = models.IntegerField(db_column='RefreshDate', blank=True, null=True)  # Field name made lowercase.
    refreshtime = models.SmallIntegerField(db_column='RefreshTime', blank=True, null=True)  # Field name made lowercase.
    school_id = models.IntegerField(db_column='SCHOOL_ID', blank=True, null=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID', blank=True, null=True)  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID', blank=True, null=True)  # Field name made lowercase.
    term_id = models.IntegerField(db_column='TERM_ID', blank=True, null=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department_id = models.IntegerField(db_column='DEPARTMENT_ID', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=60, blank=True,
                                  null=True)  # Field name made lowercase.
    mode = models.SmallIntegerField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    process = models.SmallIntegerField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    untisname = models.CharField(db_column='UntisName', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    userinfo = models.CharField(db_column='UserInfo', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    departmentrights = models.CharField(db_column='DepartmentRights', max_length=255, blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class Usergroup(models.Model, PureDjangoModel):
    user_group_id = models.SmallIntegerField(db_column='USER_GROUP_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    schools = models.CharField(db_column='Schools', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolyears = models.CharField(db_column='SchoolYears', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    versions = models.CharField(db_column='Versions', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    termnames = models.CharField(db_column='TermNames', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openschool = models.IntegerField(db_column='OpenSchool', blank=True, null=True)  # Field name made lowercase.
    openschoolyear = models.IntegerField(db_column='OpenSchoolYear', blank=True,
                                         null=True)  # Field name made lowercase.
    openversion = models.IntegerField(db_column='OpenVersion', blank=True, null=True)  # Field name made lowercase.
    useradministration = models.IntegerField(db_column='UserAdministration', blank=True,
                                             null=True)  # Field name made lowercase.
    administration = models.IntegerField(db_column='Administration', blank=True,
                                         null=True)  # Field name made lowercase.
    timetableoptimisation = models.IntegerField(db_column='TimetableOptimisation', blank=True,
                                                null=True)  # Field name made lowercase.
    rightsprint = models.IntegerField(db_column='RightsPrint', blank=True, null=True)  # Field name made lowercase.
    save2gpn = models.IntegerField(db_column='Save2gpn', blank=True, null=True)  # Field name made lowercase.
    infostp = models.IntegerField(db_column='InfoStp', blank=True, null=True)  # Field name made lowercase.
    timetable = models.SmallIntegerField(db_column='Timetable', blank=True, null=True)  # Field name made lowercase.
    masterdata = models.SmallIntegerField(db_column='MasterData', blank=True, null=True)  # Field name made lowercase.
    specialdata = models.SmallIntegerField(db_column='SpecialData', blank=True, null=True)  # Field name made lowercase.
    lesson = models.SmallIntegerField(db_column='Lesson', blank=True, null=True)  # Field name made lowercase.
    terms = models.SmallIntegerField(db_column='Terms', blank=True, null=True)  # Field name made lowercase.
    substitution = models.SmallIntegerField(db_column='Substitution', blank=True,
                                            null=True)  # Field name made lowercase.
    absences = models.SmallIntegerField(db_column='Absences', blank=True, null=True)  # Field name made lowercase.
    coursplaning = models.SmallIntegerField(db_column='Coursplaning', blank=True,
                                            null=True)  # Field name made lowercase.
    deduction = models.SmallIntegerField(db_column='Deduction', blank=True, null=True)  # Field name made lowercase.
    importdata = models.IntegerField(db_column='ImportData', blank=True, null=True)  # Field name made lowercase.
    webuntis = models.IntegerField(db_column='WebUntis', blank=True, null=True)  # Field name made lowercase.
    subststatistics = models.IntegerField(db_column='SubstStatistics', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserGroup'


class Usermessage(models.Model, PureDjangoModel):
    message_id = models.IntegerField(db_column='MESSAGE_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.
    sender_id = models.SmallIntegerField(db_column='Sender_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.SmallIntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    newmessage = models.IntegerField(db_column='NewMessage', blank=True, null=True)  # Field name made lowercase.
    notread = models.IntegerField(db_column='NotRead', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserMessage'
        unique_together = (('message_id', 'user_id'),)


class Valuecorrection(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    teacher_id = models.IntegerField(db_column='TEACHER_ID')  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='Number')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=100, blank=True, null=True)  # Field name made lowercase.
    flags = models.CharField(db_column='Flags', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    type1 = models.CharField(db_column='Type1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    value = models.IntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valueminutes = models.IntegerField(db_column='ValueMinutes', blank=True, null=True)  # Field name made lowercase.
    percentage = models.SmallIntegerField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.
    basis = models.CharField(db_column='Basis', max_length=1, blank=True, null=True)  # Field name made lowercase.
    schoolorig = models.CharField(db_column='SchoolOrig', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ValueCorrection'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'teacher_id', 'number'),)


class Version(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    counterlast = models.IntegerField(db_column='CounterLast', blank=True, null=True)  # Field name made lowercase.
    usercounterlast = models.IntegerField(db_column='UserCounterLast', blank=True,
                                          null=True)  # Field name made lowercase.
    user_idlast = models.SmallIntegerField(db_column='USER_IDLast', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    mode = models.SmallIntegerField(db_column='Mode', blank=True, null=True)  # Field name made lowercase.
    process = models.SmallIntegerField(db_column='Process', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.SmallIntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    progdate = models.CharField(db_column='ProgDate', max_length=12, blank=True,
                                null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=50, blank=True, null=True)  # Field name made lowercase.
    only1user = models.IntegerField(db_column='Only1User', blank=True, null=True)  # Field name made lowercase.
    action = models.IntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    updatedb = models.IntegerField(db_column='UpdateDb', blank=True, null=True)  # Field name made lowercase.
    readdb = models.IntegerField(db_column='ReadDb', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Version'
        unique_together = (('school_id', 'schoolyear_id', 'version_id'),)


class Views(models.Model, PureDjangoModel):
    school_id = models.IntegerField(db_column='SCHOOL_ID', primary_key=True)  # Field name made lowercase.
    schoolyear_id = models.IntegerField(db_column='SCHOOLYEAR_ID')  # Field name made lowercase.
    version_id = models.SmallIntegerField(db_column='VERSION_ID')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type')  # Field name made lowercase.
    views_id = models.IntegerField(db_column='VIEWS_ID')  # Field name made lowercase.
    owner = models.SmallIntegerField(db_column='Owner')  # Field name made lowercase.
    counter = models.IntegerField(db_column='Counter', blank=True, null=True)  # Field name made lowercase.
    user_id = models.SmallIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    sortid = models.IntegerField(db_column='SortId', blank=True, null=True)  # Field name made lowercase.
    window = models.CharField(db_column='Window', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typem = models.CharField(db_column='TypeM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fieldbool1 = models.IntegerField(db_column='FieldBool1', blank=True, null=True)  # Field name made lowercase.
    fieldbool2 = models.IntegerField(db_column='FieldBool2', blank=True, null=True)  # Field name made lowercase.
    fieldbool3 = models.IntegerField(db_column='FieldBool3', blank=True, null=True)  # Field name made lowercase.
    fieldbool4 = models.IntegerField(db_column='FieldBool4', blank=True, null=True)  # Field name made lowercase.
    fieldbool5 = models.IntegerField(db_column='FieldBool5', blank=True, null=True)  # Field name made lowercase.
    fieldbool6 = models.IntegerField(db_column='FieldBool6', blank=True, null=True)  # Field name made lowercase.
    fieldbool7 = models.IntegerField(db_column='FieldBool7', blank=True, null=True)  # Field name made lowercase.
    fieldbool8 = models.IntegerField(db_column='FieldBool8', blank=True, null=True)  # Field name made lowercase.
    fieldbool9 = models.IntegerField(db_column='FieldBool9', blank=True, null=True)  # Field name made lowercase.
    fieldbool10 = models.IntegerField(db_column='FieldBool10', blank=True, null=True)  # Field name made lowercase.
    fieldbool11 = models.IntegerField(db_column='FieldBool11', blank=True, null=True)  # Field name made lowercase.
    fieldbool12 = models.IntegerField(db_column='FieldBool12', blank=True, null=True)  # Field name made lowercase.
    fieldbool13 = models.IntegerField(db_column='FieldBool13', blank=True, null=True)  # Field name made lowercase.
    fieldbool14 = models.IntegerField(db_column='FieldBool14', blank=True, null=True)  # Field name made lowercase.
    fieldbool15 = models.IntegerField(db_column='FieldBool15', blank=True, null=True)  # Field name made lowercase.
    fieldbool16 = models.IntegerField(db_column='FieldBool16', blank=True, null=True)  # Field name made lowercase.
    fieldbool17 = models.IntegerField(db_column='FieldBool17', blank=True, null=True)  # Field name made lowercase.
    fieldbool18 = models.IntegerField(db_column='FieldBool18', blank=True, null=True)  # Field name made lowercase.
    fieldbool19 = models.IntegerField(db_column='FieldBool19', blank=True, null=True)  # Field name made lowercase.
    fieldbool20 = models.IntegerField(db_column='FieldBool20', blank=True, null=True)  # Field name made lowercase.
    fieldint1 = models.SmallIntegerField(db_column='FieldInt1', blank=True, null=True)  # Field name made lowercase.
    fieldint2 = models.SmallIntegerField(db_column='FieldInt2', blank=True, null=True)  # Field name made lowercase.
    fieldint3 = models.SmallIntegerField(db_column='FieldInt3', blank=True, null=True)  # Field name made lowercase.
    fieldint4 = models.SmallIntegerField(db_column='FieldInt4', blank=True, null=True)  # Field name made lowercase.
    fieldint5 = models.SmallIntegerField(db_column='FieldInt5', blank=True, null=True)  # Field name made lowercase.
    fieldint6 = models.SmallIntegerField(db_column='FieldInt6', blank=True, null=True)  # Field name made lowercase.
    fieldint7 = models.SmallIntegerField(db_column='FieldInt7', blank=True, null=True)  # Field name made lowercase.
    fieldint8 = models.SmallIntegerField(db_column='FieldInt8', blank=True, null=True)  # Field name made lowercase.
    fieldint9 = models.SmallIntegerField(db_column='FieldInt9', blank=True, null=True)  # Field name made lowercase.
    fieldint10 = models.SmallIntegerField(db_column='FieldInt10', blank=True, null=True)  # Field name made lowercase.
    fieldint11 = models.SmallIntegerField(db_column='FieldInt11', blank=True, null=True)  # Field name made lowercase.
    fieldint12 = models.SmallIntegerField(db_column='FieldInt12', blank=True, null=True)  # Field name made lowercase.
    fieldint13 = models.SmallIntegerField(db_column='FieldInt13', blank=True, null=True)  # Field name made lowercase.
    fieldint14 = models.SmallIntegerField(db_column='FieldInt14', blank=True, null=True)  # Field name made lowercase.
    fieldint15 = models.SmallIntegerField(db_column='FieldInt15', blank=True, null=True)  # Field name made lowercase.
    fieldint16 = models.SmallIntegerField(db_column='FieldInt16', blank=True, null=True)  # Field name made lowercase.
    fieldint17 = models.SmallIntegerField(db_column='FieldInt17', blank=True, null=True)  # Field name made lowercase.
    fieldint18 = models.SmallIntegerField(db_column='FieldInt18', blank=True, null=True)  # Field name made lowercase.
    fieldint19 = models.SmallIntegerField(db_column='FieldInt19', blank=True, null=True)  # Field name made lowercase.
    fieldint20 = models.SmallIntegerField(db_column='FieldInt20', blank=True, null=True)  # Field name made lowercase.
    fieldlong1 = models.IntegerField(db_column='FieldLong1', blank=True, null=True)  # Field name made lowercase.
    fieldlong2 = models.IntegerField(db_column='FieldLong2', blank=True, null=True)  # Field name made lowercase.
    fieldlong3 = models.IntegerField(db_column='FieldLong3', blank=True, null=True)  # Field name made lowercase.
    fieldlong4 = models.IntegerField(db_column='FieldLong4', blank=True, null=True)  # Field name made lowercase.
    fieldlong5 = models.IntegerField(db_column='FieldLong5', blank=True, null=True)  # Field name made lowercase.
    fieldlong6 = models.IntegerField(db_column='FieldLong6', blank=True, null=True)  # Field name made lowercase.
    fieldlong7 = models.IntegerField(db_column='FieldLong7', blank=True, null=True)  # Field name made lowercase.
    fieldlong8 = models.IntegerField(db_column='FieldLong8', blank=True, null=True)  # Field name made lowercase.
    fieldtext255a = models.CharField(db_column='FieldText255A', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255b = models.CharField(db_column='FieldText255B', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255c = models.CharField(db_column='FieldText255C', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255d = models.CharField(db_column='FieldText255D', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255e = models.CharField(db_column='FieldText255E', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255f = models.CharField(db_column='FieldText255F', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255g = models.CharField(db_column='FieldText255G', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext255h = models.CharField(db_column='FieldText255H', max_length=255, blank=True,
                                     null=True)  # Field name made lowercase.
    fieldtext1000a = models.CharField(db_column='FieldText1000A', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000b = models.CharField(db_column='FieldText1000B', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000c = models.CharField(db_column='FieldText1000C', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000d = models.CharField(db_column='FieldText1000D', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000e = models.CharField(db_column='FieldText1000E', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000f = models.CharField(db_column='FieldText1000F', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000g = models.CharField(db_column='FieldText1000G', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000h = models.CharField(db_column='FieldText1000H', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000i = models.CharField(db_column='FieldText1000I', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.
    fieldtext1000j = models.CharField(db_column='FieldText1000J', max_length=1000, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Views'
        unique_together = (('school_id', 'schoolyear_id', 'version_id', 'type', 'views_id', 'owner'),)
