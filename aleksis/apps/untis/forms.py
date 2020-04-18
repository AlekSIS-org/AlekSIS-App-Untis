from django import forms
from django.utils.translation import ugettext_lazy as _

from constance import config
from material import Fieldset

from aleksis.core.forms import EditGroupForm


class UntisUploadForm(forms.Form):
    untis_xml = forms.FileField(label=_("Untis XML export"))


if config.UNTIS_IMPORT_MYSQL_USE_COURSE_GROUPS:
    EditGroupForm.add_node_to_layout(Fieldset(_("UNTIS import"), "untis_subject"))
