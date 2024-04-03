# serializers.py
import googlemaps
from django.conf import settings
from rest_framework import serializers
from .models import Accommodation

class AccommodationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    def get_image_url(self, obj):
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        geocode_result = gmaps.geocode(obj.street_address)
        if geocode_result:
            location = geocode_result[0].get('geometry', {}).get('location')
            if location:
                lat = location.get('lat')
                lng = location.get('lng')
                return f"https://maps.googleapis.com/maps/api/streetview?size=400x300&location={lat},{lng}&key={settings.GOOGLE_MAPS_API_KEY}"
        return None

    class Meta:
        model = Accommodation
        fields = '__all__'
