from django.db import models

class Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="4 Series 12 Repeticiones 20 Kilos")

class Rutina(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ejercicios = models.ManyToManyField(Ejercicio)