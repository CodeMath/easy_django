from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name="index"),
    path('signup/', signup, name="signup"),
    path('signin/', auth_views.LoginView.as_view(template_name='index/signin.html'), name='signin'),
    path('signout/', auth_views.logout_then_login, {'login_url' : '/'}, name='signout'),
    path('mypage/', mypage, name="mypage")
]