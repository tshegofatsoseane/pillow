from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Accommodation
from .serializers import AccommodationSerializer

class CustomPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 1000  # Maximum page size to prevent excessive resource usage

class AccommodationSearchAPIView(ListAPIView):
    serializer_class = AccommodationSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        query = self.request.query_params.get('q')
        university = self.request.query_params.get('university')
        nearest_campus = self.request.query_params.get('nearest_campus')

        # Build the queryset with flexible filtering
        filters = Q()

        if university:
            filters &= Q(university__iexact=university)

        if nearest_campus:
            filters &= Q(nearest_campus__iexact=nearest_campus)

        if query:
            filters &= Q(street_address__icontains=query)

        return Accommodation.objects.filter(filters).order_by('id')
