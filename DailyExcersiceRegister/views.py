from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

# Create your views here.

class RegistroDiarioView(APIView):
    serializer_class = RegistroDiarioSerializer

    def get(self, request):
        detail = [{"Ejercicio": detail.plan_semanal.ejercicio.nombre, "Ejercicio id":detail.plan_semanal.ejercicio.id, "Repeticiones_hechas": detail.repeticiones_hechas, "Peso Usado (Kg)": detail.peso_usado,
                    "Fecha": detail.fecha, "Observaciones": detail.observaciones } 
        for detail in RegistroDiario.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = RegistroDiarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return RegistroDiarioView.get(self,request)
