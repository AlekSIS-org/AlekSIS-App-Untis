from django.urls import path

from . import views

urlpatterns = [
    path("import/xml/", views.xml_import, name="untis_xml_import"),
    path("groups_subjects", views.groups_subjects, name="untis_groups_subjects"),
    path("groups_child_groups", views.groups_child_groups, name="untis_groups_child_groups"),
]
