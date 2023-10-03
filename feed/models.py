from django.core.exceptions import ValidationError
from django.db import models
from menu.models import Usuario

class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.TextField()
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Publicación de {self.usuario.nombre} en Facebook"

    def clean(self):
        # Check if the user has isTrainer set to True
        if not self.usuario.isTrainer:
            raise ValidationError("Only users with isTrainer=True can create a Publicacion.")
