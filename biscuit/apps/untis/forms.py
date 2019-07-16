from django import forms
from django.utils.translation import gettext_lazy as _


class UntisUploadForm(forms.Form):
    untis_xml = forms.FileField(label=_('Untis XML export'))
