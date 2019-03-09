from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^contact/$', views.contact, name='contact'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.details, name='details'),
    url(r'^texte$', views.text, name='text'),
    url(r'^$', views.index, name='index'),
]
