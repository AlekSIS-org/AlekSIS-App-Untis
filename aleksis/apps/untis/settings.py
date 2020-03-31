from aleksis.core.util.core_helpers import lazy_config
from django.utils.translation import gettext_lazy as _

DATABASES = {
    'untis': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': lazy_config("UNTIS_NAME"),
        'USER': lazy_config("UNTIS_USER"),
        'PASSWORD': lazy_config("UNTIS_PASSWORD"),
        'HOST': lazy_config("UNTIS_HOST"),
        'PORT': lazy_config("UNTIS_PORT"),
    }
}

CONSTANCE_CONFIG = {
    "UNTIS_DB_NAME": ("untis", _("Name of database"), "char_field"),
    "UNTIS_DB_USER": ("aleksis", _("Database user"), "char_field"),
    "UNTIS_DB_PASSWORD": ("aleksis", _("Database password"), "char_field"),
    "UNTIS_DB_HOST": ("127.0.0.1", _("Database host"), "char_field"),
    "UNTIS_DB_PORT": ("3306", _("Database port"), "char_field"),
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
}

CONSTANCE_CONFIG_FIELDSETS = {
    "UNTIS import via MySQL:  Database Settings": (
        "UNTIS_DB_NAME",
        "UNTIS_DB_USER",
        "UNTIS_DB_PASSWORD",
        "UNTIS_DB_HOST",
        "UNTIS_DB_PORT",
    ),
    "UNTIS import via MySQL: Common Settings": (
        "UNTIS_IMPORT_MYSQL_UPDATE_SUBJECTS",
        "UNTIS_IMPORT_MYSQL_UPDATE_PERSONS_SHORT_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_PERSONS_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_SHORT_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_NAME",
        "UNTIS_IMPORT_MYSQL_UPDATE_GROUPS_OVERWRITE_OWNERS",
    ),
}
