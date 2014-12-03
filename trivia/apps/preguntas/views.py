from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.
def inicio(request):
	usuarios=User.objects.all()
	return render_to_response("usuarios/principal.html",{'usuarios':usuarios}, context_instace=RequestContext(request))

def registrar_temas(request):
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

def registrar_pregunta(request,id):
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
	preguntas=preguntas.objects.filter(tema=tema)
	datos={'tema':tema,'preguntas':preguntas}
	return render_to_response("preguntas/listar_preguntas.html",datos,context_instance=RequestContext(request))