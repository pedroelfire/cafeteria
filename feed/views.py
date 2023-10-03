from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class PublicacionView(APIView):
    serializer_class = PublicacionSerializer

    def get(self, request):
        detail = [{"id": detail.id,"Usuario":detail.usuario ,"Titulo": detail.titulo, "Descripcion":detail.descripcion, "Fecha": detail.fecha_publicacion}
        for detail in Publicacion.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            usuario = serializer.validated_data.get('usuario')
            if not usuario.isTrainer:
                return Response({'error': 'Only users with isTrainer=True can create a Publicacion.'}, status=400)
            serializer.save()
            return Response(serializer.data)
        
        