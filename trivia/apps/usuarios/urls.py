from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^registro/$',registro_view),
    url(r'^login/$',login_view),	
   	url(r'^base/$',base),
   	url(r'^perfil/$',base),
   	url(r'^cerrar_sesion/$',cerrar_sesion),
   	url(r'^activar/$',activar_cuenta),
)