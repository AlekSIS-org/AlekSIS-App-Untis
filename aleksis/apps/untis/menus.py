from django.utils.translation import ugettext_lazy as _

MENUS = {
    "DATA_MANAGEMENT_MENU": [
        {
            "name": _("Untis XML import"),
            "url": "untis_xml_import",
            "validators": [
                "menu_generator.validators.is_authenticated",
                "menu_generator.validators.is_superuser",
                "aleksis.core.util.core_helpers.has_person",
            ],
        }
    ]
}
