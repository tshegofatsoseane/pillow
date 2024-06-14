from django.urls import path
from .views import RegisterView, LoginView, LogoutView, StudentView, StudentUpdateView


urlpatterns = [
    path('', StudentView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('update/', StudentUpdateView.as_view()),
]