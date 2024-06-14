from django.urls import path
from .views import ListView, CreateView


urlpatterns = [
    path('', ListView.as_view()),
    path('property/<int:property_pk>/new/', CreateView.as_view()),
]
