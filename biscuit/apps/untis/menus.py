from django.utils.translation import ugettext_lazy as _

MENUS = {
    'DATA_MANAGEMENT_MENU': [
        {
            'name': _('Units import'),
            'url': 'untis_import',
            'validators': ['menu_generator.validators.is_authenticated', 'menu_generator.validators.is_superuser'],
        }
    ]
}
