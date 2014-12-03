from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
import pdb
# Create your views here.
def registro_view(request):
	if request.method=="POST":
		formulario_registro=formuser(request.POST)
		if formulario_registro.is_valid():
			nuevo_usuario=request.POST["username"]
			formulario_registro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil_registro.objects.create(user=usuario)
			return HttpResponseRedirect("/inicio/perfil/")
	else:
		formulario_registro=formuser()
	return render_to_response("usuario/registro_usuarios.html",{'formulario':formulario_registro},context_instance=RequestContext(request))
def base(request):
    return render_to_response('principal.html',{},context_instance=RequestContext(request))
#def ingresar(request):
#	#menu=permisos(request)

#	if request.method=="POST":
#		formulario=AuthenticationForm(request.POST)
#		if formulario.is_valid:
#			usuario=request.POST["username"]
#			contrasena=request.POST["password"]
#			resultado=authenticate(username=usuario, password=contrasena)
#			if resultado is not None:
#				if resultado.is_active:
#					login(request, resultado)
#					return HttpResponseRedirect("/inicio/perfil/")
#				else:
#					login(request, resultado)
#					return HttpResponseRedirect("/inicio/activar/")
#			else:
#				return HttpResponse("Nombre o contrasena son incorrectos")
#	else:	
#		formulario=AuthenticationForm()
#	return render_to_response("usuario/login.html", { "formulario":formulario},RequestContext(request))
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect("/inicio/login/")
def activar_cuenta(request):
	if request.user.is_authenticated():
		usuario=request.user
		if usuario.is_active:
			return HttpResponseRedirect("/inicio/perfil/")
		else:
			if request.method=="POST":
				usuario_modificado=User.objects.get(username=usuario)
				#pdb.set_trace()
				perfil=Perfil_registro.objects.get(user=usuario_modificado)
				formulario=formperfil(request.POST, request.FILES, instance=perfil)
				if(formulario.is_valid()):
					formulario.save()
					usuario_modificado.is_active=True
					usuario_modificado.save()
					return HttpResponseRedirect("/inicio/perfil/")
			else:
				formulario=formperfil()
			return render_to_response("usuario/activar.html", {"formulario":formulario}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/inicio/login")
def perfil_view(request):
	return render_to_response("usuario/perfil.html",{},context_instance=RequestContext(request))
def login_view(request):
	if request.method=="POST":
		formulario=AuthenticationForm(request.POST)
		if request.session['cont']>3:
			formulaio2=form_capcha(request.POST)
			if formulaio2.is_valid():
				pass
			else:
				datos={'formulario':formulario, 'formulaio2':formulaio2}
				return render_to_response("usuario/login.html", datos,context_instance=RequestContext(request))
		if formulario.is_valid()==False:
			usuario=request.POST['username']
			contrasena=request.POST['password']
			acceso=authenticate(username=usuario, password=contrasena)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					del request.session['cont']
					return HttpResponseRedirect("/perfil/")
				else:
					login(request, acceso)
					return HttpResponseRedirect("/inicio/activar/")
			else:
				request.session['cont']=request.session['cont']+1
				aux=request.session['cont']
				estado=True
				mensaje="Error en los Nombre o Contrasena Incorrectos"+str(aux)
				if(aux>3):
					formulaio2=form_capcha()
					datos={'formulario':formulario,'formulaio2':formulaio2,'estado':estado,'mensaje':mensaje}
				else:
					datos={'formulario':formulario,'estado':estado,'mensaje':mensaje}
				return render_to_response("usuario/login.html",datos,context_instance=RequestContext(request))		
	else:
		request.session['cont']=0
		formulario=AuthenticationForm()
	return render_to_response("usuario/login.html",{'formulario':formulario},context_instance=RequestContext(request))