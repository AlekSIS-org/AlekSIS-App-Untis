from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UntisConfig(AppConfig):
    name = 'biscuit.apps.untis'
    verbose_name = 'BiscuIT - ' + _('Untis interface')
