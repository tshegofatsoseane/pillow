from celery import shared_task
from .google_maps import async_get_geocode, async_get_distance_and_time
from .models import Accommodation
import asyncio

@shared_task
def fetch_geocode_and_distances(accommodation_id):
    async def async_fetch_geocode_and_distances():
        accommodation = Accommodation.objects.get(id=accommodation_id)
        street_address = accommodation.street_address

        # Fetch geocode data asynchronously
        geocode_result = await async_get_geocode(street_address)
        if not geocode_result:
            return None

        # Fetch distances and times asynchronously
        distances_and_times = await async_get_distance_and_time(street_address)

        # Here you can update the accommodation object or cache the results
        return distances_and_times
    
    return asyncio.run(async_fetch_geocode_and_distances())
