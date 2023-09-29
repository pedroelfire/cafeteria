from django.db import models
from menu.models import *
from django.contrib.auth.models import User

class Conversacion(models.Model):
    # Modelo para representar una conversación iniciada por un usuario
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Otros campos según tus necesidades

class Mensaje(models.Model):
    # Modelo para representar un mensaje en una conversación
    id = models.AutoField(primary_key=True)
    ai_role = models.BooleanField(default=True)
    conversation = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Otros campos según tus necesidades
