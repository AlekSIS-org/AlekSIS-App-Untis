MENUS = {
    'NAV_MENU_CORE': [
        {
            'name': 'Interfaces',
            'url': '#',
            'root': True,
            'submenu': [
                {
                    'name': 'Untis import',
                    'url': 'untis_import',
                    'validators': ['menu_generator.validators.is_authenticated', 'menu_generator.validators.is_superuser']
                }
            ]
        }
    ]
}
