import requests
from django.conf import settings

def geocode_address(address):
    api_key = settings.GOOGLE_MAP_API_KEY
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == 'OK':
            return result['results'][0]['geometry']['location']
    
    return None