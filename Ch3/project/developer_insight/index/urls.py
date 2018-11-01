from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('accounts/', account_session, name="account_session"),
    path('signout/',auth_views.logout_then_login, {'login_url' : '/accounts/'},name='signout',),
]