from django.contrib import admin
from django.urls import path
from .views import ForgotPasswordView, RegisterView,LoginView,LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('Login/', LoginView.as_view()),
    path('Logout/', LogoutView.as_view()),
    path('api/forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),

 ]