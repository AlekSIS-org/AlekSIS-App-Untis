from django.urls import path

from . import views


urlpatterns = [
    path('import', views.untis_import, name='untis_import'),
]
