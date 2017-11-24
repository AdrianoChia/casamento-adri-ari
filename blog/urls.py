from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^contato/', views.contato, name='contato'),
    url(r'^evento/', views.evento, name='evento'),
    url(r'^galeria/', views.galeria, name='galeria'),
    url(r'^lista_presentes/', views.lista_presentes, name='lista_presentes'),
    url(r'^rsvp/', views.rsvp, name='rsvp'),
    url(r'^lista_convidados/', views.lista_convidados, name='lista_convidados'),
    url(r'^tag/', views.hashtag, name='hashtag'),
]
