from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tema_preguntas(models.Model):
	nombre=models.CharField(max_length=200,unique=True)
	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema_preguntas)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respuesta_incorrecta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta


class permiso(models.Model):
	nombre=models.CharField(max_length=100)
	class Meta:
		permissions=(
			("add_tema","add_tema"),
			("bloques_permisos","bloques_permisos" )
		)
	def __unicode__(self):
		return self.nombre
class permisogeneral(models.Model):
	user=models.ForeignKey(User)
	permiso=models.ForeignKey(permiso)