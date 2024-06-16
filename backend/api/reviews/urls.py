from django.urls import path
from .views import ListReview, CreateReview, ReviewUpdateView, ReviewUpdateView


urlpatterns = [
    path('', ListReview.as_view()),
    path('new/', CreateReview.as_view()),
    path('<int:pk>/update/', ReviewUpdateView.as_view()),
    path('<int:pk>/delete/', ReviewUpdateView.as_view()),
]