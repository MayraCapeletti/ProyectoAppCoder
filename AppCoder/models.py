from django.db import models

# Create your models here.
# Los modelos en django son casi todos clases. Que quiero que los reconozca como modelos.


class Curso(models.Model):
    # el nombre del curso va a tener como máx 40 caracteres
    name = models.CharField(max_length=40)
    camada = models.IntegerField()
# con esto le decimos que dentro de la tabla curso pongamos dos columnas, una es nombre y la otra la camada, y el tipo de danto en caso de nombre es de tipo texto y la columna camada es de tipo numero entero


class Estudiante(models.Model):
    name = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
