from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Post (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    telefono = models.CharField(max_length=250, null=True, unique=False)
    telefono_casa = models.CharField(max_length=250, null=True,  unique=False)
    nacimiento = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=300, null=True)
    contacto_emergencia = models.CharField(max_length=250, null=True)
    telefono_emergencia = models.CharField(max_length=250, null=True)
    puesto = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)
    is_leader = models.BooleanField(default=False,null=True)

class Contacto (models.Model):
    nombre_completo = models.CharField(max_length=250, null=True)
    username = models.CharField(max_length=250, null=True)
    celular = models.CharField(max_length=250, null=True, unique=False)
    fecha_nacimiento = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=300, null=True)
    correo_electronico = models.CharField(max_length=250, null=True)
#productos,compras unitarias, totales

class compra(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='carrito', null=True)
    nombre_completo = models.CharField(max_length=250, null=True)
    celular = models.CharField(max_length=250, null=True)
    direccion= models.CharField(max_length=250, null=True, unique=False)
    correo_electronico = models.CharField(max_length=250, null=True, unique=False)
    total = models.IntegerField()

