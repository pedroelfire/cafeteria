from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

# Create your views here.

class ConversacionView(APIView):
    serializer_class = ConversacionSerializer

    def get(self, request):
        detail = [{"Id de usuario": detail.user.id, "Fecha de creacion": detail.created_at } 
        for detail in Conversacion.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = ConversacionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return ConversacionView.get(self,request)

class MensajeView(APIView):
    serializer_class = MensajeSerializer

    def get(self, request):
        detail = [{"Conversacion": detail.conversation.user.id, "Contenido": detail.content, "Fecha": detail.created_at } 
        for detail in Mensaje.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return MensajeView.get(self,request)

