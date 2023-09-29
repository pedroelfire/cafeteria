from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class AlimentoView(APIView):
    serializer_class = AlimentoSerializer

    def get(self, request):
        detail = [{"Id": detail.id,"nombre": detail.usuario.id, "Alimento": detail.nombre}
        for detail in Alimento.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = AlimentoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class ComidaView(APIView):
    serializer_class = ComidaSerializer

    def get(self, request):
        detail = [{"Id": detail.id, "Nombre": detail.nombre, "Alimentos": detail.alimentos.nombre, "Descripcion": detail.descripcion}
        for detail in Comida.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = ComidaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class DietaView(APIView):
    serializer_class = DietaSerializer

    def get(self, request):
        detail = [{"id": detail.id, "nombre": detail.nombre, "Usuario que la creo": detail.usuario.id, "Comidas": detail.comidas }
        for detail in Dieta.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = DietaSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
