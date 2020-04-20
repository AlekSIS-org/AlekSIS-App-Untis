from django.urls import path

from . import views

urlpatterns = [
    path("import/xml/", views.xml_import, name="untis_xml_import"),
]
