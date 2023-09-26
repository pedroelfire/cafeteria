from django.db import models
from menu.models import *

# Create your models here.
class RegistroDiario(models.Model):
    plan_semanal = models.ForeignKey(DetalleEjercicio, on_delete=models.CASCADE)
    repeticiones_hechas = models.IntegerField(default=0)
    peso_usado = models.FloatField(default=0.0)
    fecha = models.DateField()
    observaciones = models.TextField()