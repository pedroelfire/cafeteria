from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.utils import timezone
from django.http import JsonResponse
import openai
from register.models import *

# Create your views here.

openai_key= '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'
openai.api_key = openai_key

class ConversacionView(APIView):
    serializer_class = ConversacionSerializer

    def get(self, request):
        detail = [{"Id": detail.id, "Id de usuario": detail.user.id, "Fecha de creacion": detail.created_at } 
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
        detail = [{"conversacion id": detail.conversation.id, "Usuario id": detail.conversation.user.id, "Mensaje id": detail.id, "Contenido": detail.content, "Fecha": detail.created_at, "ai": detail.ai_role } 
        for detail in Mensaje.objects.all()]
        return Response(detail)
    
    def post(self, request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            if "content" in serializer.validated_data:
                if serializer.validated_data.get("ai_role") == False:
                    mensaje = serializer.validated_data.get("content")
                    respuesta_openai = ask_openai(mensaje)
                    nuevo_mensaje = Mensaje(
                        conversation=serializer.validated_data.get("conversation"),
                        content=respuesta_openai,  
                        created_at=timezone.now()  
                    )
                    nuevo_mensaje.save()

            return MensajeView.get(self,request)
    

def ask_openai(message):
    # Obtener todos los ejercicios creados en la tabla Ejercicio
    ejercicios = Ejercicio.objects.all()
    
    # Inicializa una lista vacía para almacenar la información de los ejercicios
    ejercicios_info = []
    
    # Comprobar si se encontraron ejercicios
    if ejercicios:
        # Recorrer los ejercicios y agregar su información a la lista ejercicios_info
        for ejercicio in ejercicios:
            ejercicios_info.append(f"{ejercicio.nombre}: {ejercicio.descripcion}")
        
        # Construir la información previa
        informacion_previa = f"Ejercicios disponibles: {', '.join(ejercicios_info)}"
        print(informacion_previa)
    else:
        informacion_previa = "No se encontraron ejercicios en la tabla Ejercicio"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente, desempeñas el trabajo de nutricionista y entrenador, tu trabajo es responder preguntas sobre esos temas."},
            {"role": "system", "content": f"Esta es la informacion previa, tomala en cuenta para tus respuestas: {informacion_previa}"},  # Agrega la información previa aquí
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer