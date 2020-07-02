from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from rules.contrib.views import permission_required

from .forms import UntisUploadForm
from .util.xml.xml import untis_import_xml


@permission_required("untis.do_xml_import")
def xml_import(request: HttpRequest) -> HttpResponse:
    context = {}

    upload_form = UntisUploadForm()

    if request.method == "POST":
        upload_form = UntisUploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            untis_import_xml(request, request.FILES["untis_xml"])

    context["upload_form"] = upload_form

    return render(request, "untis/xml_import.html", context)
