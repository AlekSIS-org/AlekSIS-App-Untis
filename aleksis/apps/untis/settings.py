from aleksis.core.settings import _settings
from django.utils.translation import gettext_lazy as _

DATABASES = {
    "untis": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": _settings.get("untis.database.name", "untis"),
        "USER": _settings.get("untis.database.user", "untis"),
        "PASSWORD": _settings.get("untis.database.password", None),
        "HOST": _settings.get("untis.database.host", "127.0.0.1"),
        "PORT": _settings.get("untis.database.port", 3306),
    }
}

CONSTANCE_CONFIG = {
    "UNTIS_IMPORT_MYSQL_UPDATE_SUBJECTS": (
        True,
        _("Update values of existing subjects?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_PERSONS_SHORT_NAME": (
        False,
        _("Update short name of existing persons?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_PERSONS_NAME": (
        False,
        _("Update first and last name of existing persons?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_SHORT_NAME": (
        False,
        _("Update short name of existing groups?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_NAME": (
        False,
        _("Update name of existing groups?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_OVERWRITE_OWNERS": (
        False,
        _("Overwrite existing owners?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_ROOMS_NAME": (
        True,
        _("Update name of existing rooms?"),
        bool,
    ),
    "UNTIS_IMPORT_MYSQL_UPDATE_SUPERVISION_AREAS": (
        True,
        _("Update values of existing supervision areas?")
    ),
    "UNTIS_IMPORT_MYSQL_USE_COURSE_GROUPS": (
        True,
        _("Build or search course groups for every course instead of setting classes as groups.")
    )
}

CONSTANCE_CONFIG_FIELDSETS = {
    "UNTIS import via MySQL: Common Settings": (
        "UNTIS_IMPORT_MYSQL_UPDATE_SUBJECTS",
        "UNTIS_IMPORT_MYSQL_UPDATE_PERSONS_SHORT_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_PERSONS_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_SHORT_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_OVERWRITE_OWNERS",
        "UNTIS_IMPORT_MYSQL_UPDATE_ROOMS_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_SUPERVISION_AREAS",
        "UNTIS_IMPORT_MYSQL_USE_COURSE_GROUPS",
    ),
}
