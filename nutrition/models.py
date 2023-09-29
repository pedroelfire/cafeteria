from django.db import models
from menu.models import *

class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    
    def __str__(self):
        return self.nombre

class Comida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    alimentos = models.ManyToManyField(Alimento, related_name='comidas')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Dieta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comidas = models.ManyToManyField(Comida, related_name='dietas')

    def __str__(self):
        return self.nombre
