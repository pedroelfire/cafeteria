from django.urls import path
from .views import *

urlpatterns = [
    path("register/", RegistroDiarioView.as_view() )
]
