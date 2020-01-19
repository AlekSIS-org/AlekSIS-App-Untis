from aleksis.core.util.core_helpers import lazy_config

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
    "UNTIS_NAME": ("untis", _("Name of database"), "char_field"),
    "UNTIS_USER": ("aleksis", _("Database user"), "char_field"),
    "UNTIS_PASSWORD": ("aleksis", _("Database password"), "char_field"),
    "UNTIS_HOST": ("127.0.0.1", _("Database host"), "char_field"),
    "UNTIS_PORT": ("3306", _("Database port"), "char_field"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "Untis Database Settings": ("UNTIS_NAME", "UNTIS_USER", "UNTIS_PASSWORD", "UNTIS_HOST", "UNTIS_PORT"),
}
