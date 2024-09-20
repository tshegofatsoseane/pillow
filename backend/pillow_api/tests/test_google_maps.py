import unittest
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'pillow_backend.test_settings'


import django
django.setup()

from pillow_api.utils.google_maps import get_geocode, get_image_url, get_map_url, get_directions_url, get_streetview_url # type: ignore

class GoogleMapsTests(unittest.TestCase):

    @patch('pillow_api.utils.google_maps.gmaps.geocode')
    def test_get_geocode(self, mock_geocode):
        mock_geocode.return_value = [{'geometry': {'location': {'lat': -25.845534, 'lng': 25.593447}}}]
        result = get_geocode('Some Location')
        self.assertEqual(result, [{'geometry': {'location': {'lat': -25.845534, 'lng': 25.593447}}}])

    @patch('pillow_api.utils.google_maps.get_geocode')
    def test_get_image_url(self, mock_geocode):
        mock_geocode.return_value = [{'geometry': {'location': {'lat': -25.845534, 'lng': 25.593447}}}]
        result = get_image_url('Some Location')
        print(f'Image URL: {result}')  
        expected_base_url = 'https://maps.googleapis.com/maps/api/streetview?size=400x300&location=-25.845534,25.593447'
        self.assertTrue(result.startswith(expected_base_url) and '&key=' in result)

    @patch('pillow_api.utils.google_maps.get_geocode')
    def test_get_map_url(self, mock_geocode):
        mock_geocode.return_value = [{'geometry': {'location': {'lat': -25.845534, 'lng': 25.593447}}}]
        result = get_map_url('Some Location')
        print(f'Map URL: {result}') 
        expected_base_url = 'https://www.google.com/maps/embed/v1/place?key='
        self.assertTrue(result.startswith(expected_base_url) and 'q=-25.845534,25.593447' in result)

    @patch('pillow_api.utils.google_maps.get_geocode')
    def test_get_directions_url(self, mock_geocode):
        mock_geocode.return_value = [{'geometry': {'location': {'lat': -25.845534, 'lng': 25.593447}}}]
        result = get_directions_url('Some Location')
        print(f'Directions URL: {result}')  
        expected_base_url = 'https://www.google.com/maps/dir/?api=1&destination=-25.845534,25.593447'
        self.assertTrue(result.startswith(expected_base_url) and '&key=' in result)

    @patch('pillow_api.utils.google_maps.get_geocode')
    def test_get_streetview_url(self, mock_geocode):
        mock_geocode.return_value = [{'geometry': {'location': {'lat': -25.845534, 'lng': 25.593447}}}]
        result = get_streetview_url('Some Location')
        print(f'Streetview URL: {result}') 
        expected_base_url = 'https://www.google.com/maps/embed/v1/streetview?key='
        self.assertTrue(result.startswith(expected_base_url) and 'location=-25.845534,25.593447' in result)

if __name__ == '__main__':
    unittest.main()
