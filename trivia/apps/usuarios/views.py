from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb
# Create your views here.


def registro_usuarios(request):
	if(request.method=="POST"):
		formuser=UserCreationForm(request.POST)
		if(formuser.is_valid()):
			formuser.save()
			return HttpResponseRedirect("/inicio/perfil/")
	formuser=UserCreationForm()
	return render_to_response("usuario/registro.html",{"formuser":formuser}, RequestContext(request))
def base(request):
    return render_to_response('base.html',{},context_instance=RequestContext(request))
def login_usuarios(request):
	if request.method=="POST":
		formlogin = AuthenticationForm(request.POST)
		if(formlogin.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username, password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/inicio/perfil/")
	formlogin=AuthenticationForm()
	return render_to_response("usuario/login.html",{"formlogin":formlogin}, RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/inicio/login/")
def perfil_usuario(request):
	return render_to_response("usuario/perfil.html",{"nombre":request.session["name"]},RequestContext(request))