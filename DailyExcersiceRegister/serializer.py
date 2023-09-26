from rest_framework import serializers
from .models import *

class RegistroDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDiario
        fields = "__all__"