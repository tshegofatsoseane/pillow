#views.py

from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Accommodation
from .serializers import AccommodationSerializer

class CustomPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Maximum page size to prevent excessive resource usage

class AccommodationSearchAPIView(ListAPIView):
    serializer_class = AccommodationSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            # If 'q' parameter is present, filter by street address
            return Accommodation.objects.filter(
                Q(street_address__icontains=query)
            ).order_by('id')
        else:
            # If 'q' parameter is not present, filter by university
            university = self.request.query_params.get('university')
            if university:
                return Accommodation.objects.filter(university__iexact=university).order_by('id')
            else:
                # Return all accommodations if no parameters are provided
                return Accommodation.objects.all().order_by('id')
