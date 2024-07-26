from rest_framework import serializers
from .models import Accommodation
from .utils.google_maps import get_image_url, get_map_url, get_directions_url, get_streetview_url
from .utils.distance_utils import calculate_distance_and_time_to_campuses

class AccommodationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    map_url = serializers.SerializerMethodField()
    directions_url = serializers.SerializerMethodField()
    streetview_url = serializers.SerializerMethodField()
    distances_and_times_to_campuses = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return get_image_url(obj.street_address)

    def get_map_url(self, obj):
        return get_map_url(obj.street_address)

    def get_directions_url(self, obj):
        return get_directions_url(obj.street_address)

    def get_streetview_url(self, obj):
        return get_streetview_url(obj.street_address)

    def get_distances_and_times_to_campuses(self, obj):
        return calculate_distance_and_time_to_campuses(obj.street_address)

    class Meta: 
        model = Accommodation
        fields = '__all__'
