from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class UsuarioView(APIView):
    serializer_class = UsuarioSerializer

    def get(self, request):
        detail = [{"id": detail.id,"nombre": detail.nombre}
        for detail in Usuario.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class PlanView(APIView):
    serializer_class = PlanSerializer

    def get(self, request):
        detail = [{"usuario": detail.usuario.id, "semana": detail.semana, "dia_semana": detail.dia_semana, "fecha": detail.fecha}
        for detail in PlanSemanal.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return PlanView.get(self,request)

class EjercicioView(APIView):
    serializer_class = EjercicioSerializer

    def get(self, request):
        detail = [{"id": detail.id, "nombre": detail.nombre}
        for detail in Ejercicio.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = EjercicioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return EjercicioView.get(self,request)
        
class DetalleEjercicioView(APIView):
    serializer_class = DetalleEjercicioSerializer

    def get(self, request):
        detail = [{"Plan Semanal": detail.plan_semanal.dia_semana, "Ejercicio": detail.ejercicio.nombre , 
                   "Repeticiones": detail.repeticiones, "Series": detail.series, "Peso": detail.peso, "Tipo de equipo": detail.tipo_equipo}
        for detail in DetalleEjercicio.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = DetalleEjercicioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return DetalleEjercicioView.get(self,request)

        