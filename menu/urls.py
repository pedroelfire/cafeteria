from django.urls import path
from .views import *

urlpatterns = [
    path("usuario/",UsuarioView.as_view() )
]
