from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class UsuarioView(APIView):
    serializer_class = UsuarioSerializer

    def get(self, request):
        detail = [{"id": detail.id,"Entrenador":detail.isTrainer,"nombre": detail.nombre}
        for detail in Usuario.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
