from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path('login/', views.view_login, name="login"),
    path('register/', views.PublicRegisterView.as_view(), name='register'),
    path('register_confirmation', views.EmailConfirmationView.as_view(), name='email_confirmation'),
    path('register_adm/', views.superuser_form, name='register-adm'),
    path("logout/", auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name="logout"),
]