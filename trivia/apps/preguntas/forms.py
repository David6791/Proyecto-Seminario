from django.forms import ModelForm
from django import forms
from .models import *

class formulario_tema(ModelForm):
	class Meta:
		model=Tema_preguntas

class formulario_pregunta(ModelForm):
	nombre=forms.CharField(required=True,label="Preguntas :")
	class Meta:
		model=Pregunta
		exclude=['tema']
class formulario_respuesta(ModelForm):
	class Meta:
		model=Respuesta
		exclude=["pregunta"]

class PermisoForm(ModelForm):
	class Meta:
		model=permiso
class PermisosgeForms(ModelForm):
	class Meta:
		model=permisogeneral