from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^$',inicio, name='Inicio'),
    url(r'^registro_tema/$',registrar_temas),
    url(r'^registro_pregunta/(\d+)/$',registrar_pregunta),
)