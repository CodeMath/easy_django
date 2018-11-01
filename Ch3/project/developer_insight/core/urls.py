from django.urls import path
from .views import *

urlpatterns = [
    path('reply/<int:id>/', reply, name="reply"),
    path('vote/<int:id>/<str:vote_type>/', article_vote, name="article_vote"),
]