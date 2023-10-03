from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class EjercicioView(APIView):
    serializer_class = EjercicioSerializer

    def get(self, request):
        detail = [{"id": detail.id,"nombre":detail.nombre,"descripcion": detail.descripcion}
        for detail in Ejercicio.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = EjercicioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class RutinaView(APIView):
    serializer_class = RutinaSerializer

    def get(self, request):
        details = []
        for detail in Rutina.objects.all():
            ejercicio_details = []
            for ejercicio_en_rutina in detail.ejercicios.all():
                ejercicio_detail = {
                    "nombre": ejercicio_en_rutina.nombre,
                    "descripcion": ejercicio_en_rutina.descripcion  # Agrega la descripción del ejercicio
                }
                ejercicio_details.append(ejercicio_detail)

            rutina_detail = {
                "id": detail.id,
                "nombre": detail.nombre,
                "ejercicios": ejercicio_details
            }
            details.append(rutina_detail)

        return Response(details)

    def post(self, request):
        serializer = RutinaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
