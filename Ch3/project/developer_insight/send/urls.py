from django.urls import path
from .views import *

urlpatterns = [
    path('send/', SendMessage, name="SendMessage"),
]