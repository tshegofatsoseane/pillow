import requests
from django.conf import settings

def get_geocode(street_address):
    url = f"https://geocode.search.hereapi.com/v1/geocode?q={street_address}&apiKey={settings.HERE_MAPS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        items = response.json().get('items', [])
        if items:
            return items[0]
    return None

def get_image_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result.get('position')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://image.maps.ls.hereapi.com/mia/1.6/mapview?c={lat},{lng}&z=14&w=400&h=300&apiKey={settings.HERE_MAPS_API_KEY}"
    return None

def get_map_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result.get('position')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://www.here.com/?map={lat},{lng},14,normal&apiKey={settings.HERE_MAPS_API_KEY}"
    return None

def get_directions_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result.get('position')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://wego.here.com/directions/mix/{lat},{lng}?map={lat},{lng},14,normal&apiKey={settings.HERE_MAPS_API_KEY}"
    return None

def get_streetview_url(street_address):
    geocode_result = get_geocode(street_address)
    if geocode_result:
        location = geocode_result.get('position')
        if location:
            lat = location.get('lat')
            lng = location.get('lng')
            return f"https://maps.ls.hereapi.com/maptile/2.1/maptile/newest/normal.day/{lat},{lng}/14/256/png8?apiKey={settings.HERE_MAPS_API_KEY}"
    return None
