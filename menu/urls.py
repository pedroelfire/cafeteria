from django.urls import path
from .views import *

urlpatterns = [
    path("usuario/",UsuarioView.as_view() ),
    path("plan/", PlanView.as_view()),
    path("ejercicio/", EjercicioView.as_view()),
    path("detalle/", DetalleEjercicioView.as_view())
]
