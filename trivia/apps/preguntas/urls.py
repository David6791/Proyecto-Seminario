from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    #url(r'^$',inicio, name='Inicio'),
    url(r'^registro_tema/$',registrar_temas),
    url(r'^registro_pregunta/(\d+)/$',registrar_pregunta),
    url(r'^listar_preguntas/(\d+)/$',listar_preguntas),
    url(r'^editar_preguntas/(\d+)/$',registrar_pregunta),
    url(r'^permisoss/$',permiso),
    url(r'^permisosg/$',permisogeneral),
)