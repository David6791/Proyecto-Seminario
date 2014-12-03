from django.db import models

# Create your models here.

class Tema_preguntas(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.nombre

class preguntas(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema_preguntas)
	def __str__(self):
		return self.nombre

class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respuesta_incorrecta=models.CharField(max_length=500)
	pregunta=models.ForeignKey(preguntas)
	def __str__(self):
		return self.pregunta