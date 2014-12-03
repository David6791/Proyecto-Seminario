from .thumbs import ImageWithThumbsField
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
# Create your models here.
class Perfil_registro(models.Model):
	user=models.OneToOneField(User,unique=True)
	avatar=ImageWithThumbsField(upload_to="img_user", sizes=(75,75))