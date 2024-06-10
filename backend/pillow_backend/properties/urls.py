from django.urls import path
from .views import PropertyListView, RegisterView, PropertyUpdateView, PropertyDeleteView


urlpatterns = [
    path('', PropertyListView.as_view()),
    path('new/', RegisterView.as_view()),
    path('<int:pk>/update/', PropertyUpdateView.as_view()),
    path('<int:pk>/delete/', PropertyDeleteView.as_view()),
]