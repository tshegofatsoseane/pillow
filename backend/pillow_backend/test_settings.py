from decouple import config

DEBUG = True
GOOGLE_MAPS_API_KEY = config('GOOGLE_MAPS_API_KEY', default='api_key')

