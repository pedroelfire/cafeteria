from django.urls import path
from .views import *

urlpatterns = [
    path("mensaje/", MensajeView.as_view() ),
    path("conversacion/", ConversacionView.as_view()),

]
