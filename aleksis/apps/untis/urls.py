from django.urls import path

from . import views

urlpatterns = [
    path("import/xml/", views.xml_import, name="untis_xml_import"),
    path("import/mysql/", views.mysql_import, name="untis_mysql_import"),
]
