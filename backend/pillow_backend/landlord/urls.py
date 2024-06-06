from django.urls import path
from .views import register, logout_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='landlord-register'),
    path('login/', auth_views.LoginView.as_view(template_name='landlord/login.html'), name='landlord-login'),
    path('logout/', logout_views, name='landlord-login'),
]