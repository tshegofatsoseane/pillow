from celery import shared_task
from .google_maps import get_geocode, get_distance_and_time
from .models import Accommodation

@shared_task
def fetch_geocode_and_distances(accommodation_id):
    accommodation = Accommodation.objects.get(id=accommodation_id)
    street_address = accommodation.street_address

    # Fetch geocode data
    geocode_result = get_geocode(street_address)
    if not geocode_result:
        return None

    # Fetch distances and times
    distances_and_times = get_distance_and_time(street_address)

    # Here you can update the accommodation object or cache the results
    return distances_and_times
