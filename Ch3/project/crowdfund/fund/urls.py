from django.urls import path
from .views import *

urlpatterns = [
    path('funding/new/', register, name="register"),
    path('funding/<int:id>/', view_funding, name="view_funding"),
    path('funding/update/<int:id>/', funding_news, name="funding_news"),
    path('funding/add/reward/<int:id>/', add_reward, name="add_reward"),
]