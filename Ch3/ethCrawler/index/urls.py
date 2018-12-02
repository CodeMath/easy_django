from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('data/', get_data, name="get_data"),
]
