#views.py

from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Accommodation
from .serializers import AccommodationSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5  # You can adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Maximum page size to prevent excessive resource usage

class AccommodationSearchAPIView(ListAPIView):
    serializer_class = AccommodationSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return Accommodation.objects.filter(
                Q(street_address__icontains=query)
            ).order_by('id')  # Add ordering by 'id'
        else:
            return Accommodation.objects.all().order_by('id')  # Add ordering by 'id'
