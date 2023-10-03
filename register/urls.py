from django.urls import path
from .views import *

urlpatterns = [
    path("ejercicio/",EjercicioView.as_view() ),
    path("rutina/", RutinaView.as_view()),
]
