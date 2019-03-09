from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^details/(?P<pk>[0-9]+)$', views.details, name='details'),
    path('texte', views.text, name='text'),
    path('', views.index, name='index'),
]
