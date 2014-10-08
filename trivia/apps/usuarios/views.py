from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
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
			return HttpResponseRedirect("/inicio/registro/")
	formuser=UserCreationForm()
	return render_to_response("usuario/registro.html", {"formuser":formuser}, RequestContext(request))