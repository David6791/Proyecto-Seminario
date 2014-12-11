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
			#return HttpResponse(usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponseRedirect("/perfil/")
	else:
		formulario_registro=formuser()
	return render_to_response("usuario/registro_usuarios.html",{'formulario':formulario_registro},context_instance=RequestContext(request))
def principal(request):
	return render_to_response('principal.html',{},RequestContext(request))
def jugar(request):
	return render_to_response('jugar.html',{},context_instance=RequestContext(request))
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
	return HttpResponseRedirect("/login/")
#def activar_cuenta(request):
#	if request.user.is_authenticated():
#		usuario=request.user
#		if usuario.is_active:
#			return HttpResponseRedirect("/inicio/perfil/")
#		else:
#			usuario_modificado=User.objects.get(username=usuario)
#			perfil=Perfil_registro.objects.get(user=usuario_modificado)
#			if request.method=="POST":
#				#pdb.set_trace()
#				formulario=formperfil(request.POST, request.FILES, instance=perfil)
#				if formulario.is_valid():
#					formulario.save()
#	 				usuario_modificado.is_active=True
#					usuario_modificado.save()
#					return HttpResponseRedirect("/inicio/perfil/")
#			else:
#				formulario=formperfil(instance=perfil)
#			return render_to_response("usuario/activar.html", {"formulario":formulario}, context_instance=RequestContext(request))
#	else:
#		return HttpResponseRedirect("/inicio/login")

def user_active_view(request):
	if request.user.is_authenticated():
		u=request.user
		if u.is_active:
			return HttpResponseRedirect("/perfil/")
		else:
			if request.method=="POST":
				usuario=User.objects.get(username=u)
				perfil=Perfil.objects.get(user=usuario)
				formulario=fperfil(request.POST,request.FILES,instance=perfil)
				if formulario.is_valid():
					formulario.save()
					usuario.is_active=True
					usuario.save()
					return HttpResponseRedirect("/perfil/")
			else:
				formulario=fperfil()
			return render_to_response("usuario/activar.html",{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")

def perfil_view(request):
	usu=request.user
	usuario=User.objects.get(username=usu)
	perfil=Perfil.objects.get(user=usuario)
	return render_to_response("usuario/perfil.html",{'perfil':perfil},context_instance=RequestContext(request))
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
					return HttpResponseRedirect("/activar/")
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

def editar_perfil(request):
	if request.user.is_authenticated():
		u=request.user
		usuario=User.objects.get(username=u)
		perfil=Perfil.objects.get(user=usuario)
		if request.method=='POST':
			formulario=formuser_modificar(request.POST,request.FILES,instance=perfil)
			if formulario.is_valid():
				formulario.save()
				return HttpResponseRedirect("/perfil/")
		else:
			formulario=formuser_modificar(instance=perfil)
			return render_to_response('editar_perfil.html',{'formulario':formulario},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")
