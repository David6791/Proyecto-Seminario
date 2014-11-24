from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^registro/$',registro_usuarios),	
    url(r'^login/$',login_usuarios),
    url(r'^perfil/$',perfil_usuario),
   	url(r'^logout/$',logout_usuario),
   	url(r'^base/$',base),

  )