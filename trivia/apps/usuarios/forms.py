from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import pdb
from captcha.fields import ReCaptchaField
class formperfil(ModelForm):
	class Meta:
		model=Perfil_registro
		exclude=['user']
class formuser(UserCreationForm):
	username=forms.CharField(max_length=40, required=True, help_text=False, label="Nick")
	password2=forms.CharField(help_text=False, label="Repass", widget=forms.PasswordInput)
	first_name=forms.CharField(max_length=50, required=True, label="Nombre")
	last_name=forms.CharField(max_length=50, required=True, label="Apellido")
	email=forms.EmailField(max_length=100, required=True, label="Email")
	class Meta:
		model=User
		fields=("username", "password1", "password2", "first_name", "last_name", "email")
	def save(self, commit=True):
		user=super(formuser,self).save(commit=False)
		user.first_name=self.cleaned_data.get("first_name")
		user.last_name=self.cleaned_data.get("last_name")
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return user
class form_capcha(forms.Form):
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})