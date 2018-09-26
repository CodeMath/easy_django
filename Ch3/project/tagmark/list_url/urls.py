# list_url/urls.py
from django.urls import path
from .views import *

urlpatterns = [

    # path('list/', List_url.as_view(), name='List_url'),
    path('list/', Search_ListView.as_view(), name='List_url'),
]