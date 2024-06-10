from rest_framework import serializers
from .models import Accommodation
from utils.google_maps import get_image_url, get_map_url, get_directions_url, get_streetview_url

class AccommodationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    map_url = serializers.SerializerMethodField()
    directions_url = serializers.SerializerMethodField()
    streetview_url = serializers.SerializerMethodField()
    
    def get_image_url(self, obj):
        return get_image_url(obj.street_address)

    def get_map_url(self, obj):
        return get_map_url(obj.street_address)

    def get_directions_url(self, obj):
        return get_directions_url(obj.street_address)
    
    def get_streetview_url(self, obj):
        return get_streetview_url(obj.street_address)

    class Meta: 
        model = Accommodation
        fields = '__all__'
