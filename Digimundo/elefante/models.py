from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Alumnos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    nombre = models.CharField(max_length=250, null=True)
    apellido = models.CharField(max_length=250, null=True)
    celular = models.CharField(max_length=250, null=True, unique=False)
    correo = models.CharField(max_length=250, null=True,  unique=False)
    fecha_nacimiento = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=300, null=True)
    carrera = models.CharField(max_length=250, null=True)
    edificio = models.CharField(max_length=250, null=True)
    recurse = models.BooleanField(default=False,null=True)
