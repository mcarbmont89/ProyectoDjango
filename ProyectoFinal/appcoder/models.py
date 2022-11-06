from django.db import models
from datetime import datetime

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    camada=models.IntegerField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    profesion=models.CharField(max_length=40)

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)

class Entregable(models.Model):
    nombre=models.CharField(max_length=40)
    fechaDeEntrega=models.DateField(("Date"), default=datetime.now())
    entregado=models.BooleanField(default=False)

class Familiares(models.Model):
    nombre=models.CharField(max_length=40)
    fechaDeNacimiento=models.DateField(("Date"), default=datetime.now())
    ciudad=models.CharField(max_length=40)