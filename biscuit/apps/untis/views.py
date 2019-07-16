from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UntisUploadForm
from .util import untis_import_xml

from biscuit.core.decorators import admin_required


@login_required
@admin_required
def untis_import(request):
    context = {}

    upload_form = UntisUploadForm()

    if request.method == 'POST':
        upload_form = UntisUploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            untis_import_xml(request, request.FILES['untis_xml'])

    context['upload_form'] = upload_form

    return render(request, 'untis/untis_import.html', context)
