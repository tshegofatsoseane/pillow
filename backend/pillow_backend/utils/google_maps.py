import googlemaps
from django.conf import settings

gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

def get_geocode(street_address):
    return gmaps.geocode(street_address)

def get_image_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result[0].get('geometry', {}).get('location')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://maps.googleapis.com/maps/api/streetview?size=400x300&location={lat},{lng}&key={settings.GOOGLE_MAPS_API_KEY}"
    return None

def get_map_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result[0].get('geometry', {}).get('location')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://www.google.com/maps/embed/v1/place?key={settings.GOOGLE_MAPS_API_KEY}&q={lat},{lng}"
    return None

def get_directions_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result[0].get('geometry', {}).get('location')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://www.google.com/maps/dir/?api=1&destination={lat},{lng}&key={settings.GOOGLE_MAPS_API_KEY}"
    return None

def get_streetview_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result[0].get('geometry', {}).get('location')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            encoded_address = f"{lat},{lng}"
            return f"https://www.google.com/maps/embed/v1/streetview?key={settings.GOOGLE_MAPS_API_KEY}&location={encoded_address}"
    return None
