from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class PlanSemanal(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    semana = models.IntegerField()
    dia_semana = models.CharField(max_length=20)
    fecha = models.DateField()

class Ejercicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class DetalleEjercicio(models.Model):
    plan_semanal = models.ForeignKey(PlanSemanal, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    repeticiones = models.IntegerField()
    series = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_equipo = models.CharField(max_length=50)
