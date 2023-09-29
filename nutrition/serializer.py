from rest_framework import serializers
from .models import *

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = "__all__"

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comida
        fields = "__all__"

class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = "__all__"