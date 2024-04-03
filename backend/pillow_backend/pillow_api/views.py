from django.db.models import Q
from rest_framework.generics import ListAPIView
from .models import Accommodation
from .serializers import AccommodationSerializer

class AccommodationSearchAPIView(ListAPIView):
    serializer_class = AccommodationSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return Accommodation.objects.filter(
                Q(street_address__icontains=query)
            )
        else:
            return Accommodation.objects.all()
