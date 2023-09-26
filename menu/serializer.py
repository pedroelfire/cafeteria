from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanSemanal
        fields = "__all__"

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = "__all__"

class DetalleEjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleEjercicio
        fields = "__all__"