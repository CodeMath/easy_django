# get_url/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('', register_url, name='register_url'),
    path('', Generic_register_url.as_view(), name='register_url'),
]