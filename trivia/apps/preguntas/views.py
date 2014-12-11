from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.
#def inicio(request):
#	usuarios=User.objects.all()
#	return render_to_response("usuarios/principal.html",{'usuarios':usuarios}, context_instace=RequestContext(request))

def registrar_temas(request):
	if request.user.is_authenticated():
		titulo="Registro de Temas"
		temas=Tema_preguntas.objects.all()
		if request.method=="POST":
			formulario=formulario_tema(request.POST)
			if formulario.is_valid():
				formulario.save()
				estado=True
				datos={'titulo':titulo, 'formulario':formulario, 'estado':estado, 'temas':temas}
				return render_to_response("preguntas/registro_temas.html",datos,context_instance=RequestContext(request))
		else:
			formulario=formulario_tema()
		datos={'titulo':titulo,'formulario':formulario, 'temas':temas}
		return render_to_response("preguntas/registro_temas.html",datos,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect("/login/")

def registrar_pregunta(request,id):
	usuario=request.user
	if not usuario.has_perm("preguntas.add_pregunta"):
		return HttpResponse("Usted no tiene per")
	tema=Tema_preguntas.objects.get(id=int(id))
	titulo="Resgistrar temas a :"+tema.nombre
	titulo2="Registre las Respuestas"
	if request.method=="POST":
		formulario=formulario_pregunta(request.POST)
		formulario2=formulario_respuesta(request.POST)
		if formulario.is_valid() and formulario2.is_valid():
			pregunta=formulario.save(commit=False)
			pregunta.tema=tema
			pregunta.save()
			respuesta=formulario2.save(commit=False)
			respuesta.pregunta=pregunta
			respuesta.save()
			estado=True
			formulario=formulario_pregunta()
			datos={'titulo':titulo,'formulario':formulario,'estado':estado,'titulo2':titulo2,'formulario2':formulario2}
			return render_to_response("preguntas/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=formulario_pregunta()
		formulario2=formulario_respuesta()
	datos={'titulo':titulo,'titulo2':titulo2,'formulario':formulario,'formulario2':formulario2}	
	return render_to_response("preguntas/registro_preguntas.html",datos,context_instance=RequestContext(request))

def listar_preguntas(request,id):
	tema=Tema_preguntas.objects.get(id=int(id))
	preguntas=Pregunta.objects.filter(tema=tema)
	datos={'tema':tema,'preguntas':preguntas}
	return render_to_response("preguntas/listar_preguntas.html",datos,context_instance=RequestContext(request))

def eliminar_pregunta(request, id):
	id=pregunta.tema.id
	respuestas=Res_correcta.objects.get(pregunta=pregunta)
	pregunta.delete()
	return HttpResponseRedirect("/preguntas/editar_preguntas/"+str(id)+"/")

def editar_preguntas(request,id):
	pregunta=Pregunta.objects.get(id=int(id))
	respuesta=Respuesta.objects.get(pregunta=pregunta)
	if request.method=="POST":
		formulario=formulario_pregunta(request.POST,instance=pregunta)
		formulario2=formulario_respuesta(request.POST,instance=respuesta)
		if formulario.is_valid() and formulario2.is_valid():
			formulario.save()
			formulario2.save()
			estado=True
			datos={'formulario':formulario,'estado':estado,'formulario2':formulario2}
			return render_to_response("principal/registro_preguntas.html",datos,context_instance=RequestContext(request))
	else:
		formulario=formulario_pregunta(instance=pregunta)
		formulario2=formulario_respuesta(instance=respuesta)
	datos={'formulario':formulario,'formulario2':formulario2}
	return render_to_response("/registro_preguntas.html",datos,context_instance=RequestContext(request))


def permisos(request):
	lista_permisos=[]
	if request.user.has_perm("usuario.add_temas"):
		lista_permisos.append({"url":"/tema/","label":"Regsitro Temas"})
	if request.user.has_perm("usuario.bloques_permisos"):
		lista_permisos.append({"url":"/permisosg/","label":"Permisos"})
	return lista_permisos
def permiso(request):
	menu=permisos(request)
	usuario=request.user
	if not usuario.has_perm("usuario.add_tema"):
		estado=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estado, "mensaje":mensaje,"menu":menu}
		return render_to_response("permisos/permiso.html",datos, RequestContext(request))
	if request.user.is_authenticated():
		if request.method=="POST":
			form_perm=PermisoForm(request.POST)
			if form_perm.is_valid():
				form_perm.save()
			estadoo=True
			mensaje="se a registrado permiso con exito"
			dato={"menu":menu,"form_perm":form_perm, "mensaje":mensaje, "estadoo":estadoo}
			return render_to_response("permisos/permiso.html",dato,RequestContext(request))	
		else:
			form_perm=PermisoForm()
		return render_to_response("permisos/permiso.html",{"menu":menu,"form_perm":form_perm},RequestContext(request))
	return HttpResponseRedirect("/login/")
def permisogeneral(request):
	menu=permisos(request)
	usuario=request.user
	if not usuario.has_perm("usuario.add_tema"):
		estado=True
		mensaje="Error no puede acceder a este sitio no tiene permisos"
		datos={"estadoo":estado, "mensaje":mensaje,"menu":menu}
		return render_to_response("permisos/permiso.html",datos, RequestContext(request))
	if request.user.is_authenticated():
		if request.method=="POST":
			form_permg=PermisosgeForms(request.POST)
			if form_permg.is_valid():
				nombre=form_permg.save(commit=False)
				nombre.save()
				name=nombre.user
				if(nombre.permiso.nombre=="add_tema"):
					i=48
				else:
					if(nombre.permiso.nombre=="bloques_permisos"):
						i=49
				name.user_permissions.add(i)
				estadoo=True
				mensaje="se a registrado permiso con exito"
				dato={"menu":menu,"form_permg":form_permg, "mensaje":mensaje, "estadoo":estadoo}
				return render_to_response("permisos/permisogeneral.html",dato,RequestContext(request))
				
		else:
			form_permg=PermisosgeForms()
		return render_to_response("permisos/permisogeneral.html",{"menu":menu,"form_permg":form_permg},RequestContext(request))
	return HttpResponseRedirect("/login/")