from django.urls import path
from .views import AccommodationSearchAPIView

urlpatterns = [
    path('accommodations/', AccommodationSearchAPIView.as_view(), name='accommodations-search'),
]
