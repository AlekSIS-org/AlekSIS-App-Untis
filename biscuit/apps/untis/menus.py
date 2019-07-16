from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from menu import Menu, MenuItem


menu_items = [
    MenuItem(_('Datenimport'),
             reverse('untis_import'),
             check=lambda request: request.user.is_authenticated and request.user.is_superuser),
]

app_menu = MenuItem('Untis',
                    '#',
                    children=menu_items)

Menu.add_item(_('Interfaces'), app_menu)
