from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('board/', Board_View.as_view(), name="All_Board_View"),
    path('board/<int:id>/', Board_View.as_view(), name="Board_View" ),
    path('board/<int:id>/view/<int:pk>/', Article_View.as_view(), name="Article_View"),
    path('board/<int:id>/new/', login_required(Create_Article_View.as_view(), login_url='account_session'), name="Create_Article_View"),
    path('board/<int:pk>/edit/', login_required(Update_Article_View.as_view(), login_url='account_session'), name="Update_Article_View"),
]