# serializers.py
import googlemaps
from django.conf import settings
from rest_framework import serializers
from .models import Accommodation

class AccommodationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    map_url = serializers.SerializerMethodField()
    directions_url = serializers.SerializerMethodField()
    streetview_url = serializers.SerializerMethodField()
    
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

    def get_map_url(self, obj):  # Corrected method name
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        geocode_result = gmaps.geocode(obj.street_address)
        if geocode_result:
            location = geocode_result[0].get('geometry', {}).get('location')
            if location:
                lat = location.get('lat')
                lng = location.get('lng')
                return f"https://www.google.com/maps/embed/v1/place?key={settings.GOOGLE_MAPS_API_KEY}&q={lat},{lng}"
        return None      

    def get_directions_url(self, obj):
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        geocode_result = gmaps.geocode(obj.street_address)
        if geocode_result:
            location = geocode_result[0].get('geometry', {}).get('location')
            if location:
                lat = location.get('lat')
                lng = location.get('lng')
                api_key = settings.GOOGLE_MAPS_API_KEY
                return f"https://www.google.com/maps/dir/?api=1&destination={lat},{lng}&key={api_key}"
        return None
    
    def get_streetview_url(self, obj):
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
        geocode_result = gmaps.geocode(obj.street_address)
        if geocode_result:
            location = geocode_result[0].get('geometry', {}).get('location')
            if location:
                lat = location.get('lat')
                lng = location.get('lng')
                encoded_address = f"{lat},{lng}"
                return f"https://www.google.com/maps/embed/v1/streetview?key={settings.GOOGLE_MAPS_API_KEY}&location={encoded_address}"

    class Meta: 
        model = Accommodation
        fields = '__all__'
