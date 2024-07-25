from .google_maps import get_geocode
import googlemaps
from django.conf import settings

gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

CAMPUS_ADDRESSES = {
    'Mafikeng': 'North West University Mahikeng, Mmabatho Unit 5, Mahikeng, 2790',
    'Potchefstroom': 'NWU Potchefstroom Campus Student Centre, 2 Hoffman St, Potchefstroom, 2520',
    'Vanderbijlpark': 'North-West University Vaal Triangle Campus, 1174 Hendrick Van Eck Boulevard, Vanderbijlpark, 1900'
}

def calculate_distance_and_time_to_campuses(street_address):
    """
    Calculate the distance and time from the given address to each campus for driving and walking.
    """
    results = {}

    # get geocode location of the accommodation
    accommodation_location = get_geocode(street_address)
    
    if not accommodation_location:
        return None

    accommodation_coords = accommodation_location[0].get('geometry', {}).get('location')

    for campus_name, campus_address in CAMPUS_ADDRESSES.items():
        # get geocode location of the campus
        campus_location = get_geocode(campus_address)

        if campus_location:
            campus_coords = campus_location[0].get('geometry', {}).get('location')
            results[campus_name] = {}

            for mode in ["driving", "walking"]:
                distance_result = gmaps.distance_matrix(
                    origins=[accommodation_coords],
                    destinations=[campus_coords],
                    mode=mode
                )

                if distance_result['rows'][0]['elements'][0]['status'] == 'OK':
                    distance = distance_result['rows'][0]['elements'][0]['distance']['text']
                    duration = distance_result['rows'][0]['elements'][0]['duration']['text']
                    results[campus_name][mode] = {
                        'distance': distance,
                        'duration': duration
                    }

    return results
