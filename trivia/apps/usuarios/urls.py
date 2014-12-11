from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:

    url(r'^$',principal),
    url(r'^registro/$',registro_view),
    url(r'^login/$',login_view),	
   	url(r'^jugar/$',jugar),
   	url(r'^perfil/$',perfil_view),
   	url(r'^cerrar_sesion/$',cerrar_sesion),
   	url(r'^activar/$',user_active_view),
   	url(r'^editar_perfil/$',editar_perfil),
)