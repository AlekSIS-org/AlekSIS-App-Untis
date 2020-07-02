from django import forms
from django.utils.translation import ugettext_lazy as _

from material import Fieldset

from aleksis.core.forms import EditGroupForm
from aleksis.core.models import Group


class UntisUploadForm(forms.Form):
    untis_xml = forms.FileField(label=_("Untis XML export"))
