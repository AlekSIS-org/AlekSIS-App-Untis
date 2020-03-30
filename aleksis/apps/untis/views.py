from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from aleksis.core.decorators import admin_required

from .forms import UntisUploadForm
from aleksis.apps.untis.util.xml.xml import untis_import_xml


@login_required
@admin_required
def xml_import(request: HttpRequest) -> HttpResponse:
    context = {}

    upload_form = UntisUploadForm()

    if request.method == "POST":
        upload_form = UntisUploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            untis_import_xml(request, request.FILES["untis_xml"])

    context["upload_form"] = upload_form

    return render(request, "untis/xml_import.html", context)
