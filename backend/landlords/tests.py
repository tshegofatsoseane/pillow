from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .models import Landlord


class LandlordAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('landlord-register')
        self.login_url = reverse('landlord-login')
        
        self.user_data = {
            'email': 'jdoe@yahoo.com',
            'password': 'my_password'
        }
        
    def test_register(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        