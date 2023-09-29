from django.urls import path
from .views import *

urlpatterns = [
    path("alimento/", AlimentoView.as_view() ),
    path("comida/", ComidaView.as_view()),
    path("dieta/", DietaView.as_view())

]
