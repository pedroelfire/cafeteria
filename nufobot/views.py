from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.utils import timezone
from django.http import JsonResponse
import openai
from menu.models import *

# Create your views here.

openai_key= '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'
openai.api_key = openai_key

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
        detail = [{"conversacion id": detail.conversation.id, "Usuario id": detail.conversation.user.id, "Mensaje id": detail.id, "Contenido": detail.content, "Fecha": detail.created_at } 
        for detail in Mensaje.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if "content" in serializer.validated_data:
                mensaje = serializer.validated_data.get("content")
                respuesta_openai = ask_openai(mensaje)
                nuevo_mensaje = Mensaje(
                    conversation=serializer.validated_data.get("conversation"),
                    content=respuesta_openai,  
                    created_at=timezone.now()  
                )
                nuevo_mensaje.save()

            return redirect("http://127.0.0.1:8000/nufobot/mensaje/")
        

def ask_openai(message):
    detalles_info = DetalleEjercicio.objects.filter(plan_semanal__usuario_id=1)
    informacion_previa = "\n".join([
    f"Usuario: {detalle.plan_semanal.usuario.nombre}, Ejercicio: {detalle.ejercicio.nombre}, Repeticiones: {detalle.repeticiones}, Series: {detalle.series}, Peso: {detalle.peso}, Tipo de Equipo: {detalle.tipo_equipo}"
    for detalle in detalles_info
])
    response = openai.ChatCompletion.create(
        model = "gpt-4",
    messages=[
        {"role": "system", "content": "You are an helpful assistant."},
        {"role": "system", "content": informacion_previa},  # Agrega la información previa aquí
        {"role": "user", "content": message},
    ]
)
    
    answer = response.choices[0].message.content.strip()
    return answer