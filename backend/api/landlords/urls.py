from django.urls import path
from .views import RegisterView, LoginView, LogoutView, LandlordView, LandlordUpdateView


urlpatterns = [
    path('', LandlordView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('update/', LandlordUpdateView.as_view()),
]