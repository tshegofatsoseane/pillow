import os
import jwt
from .models import Amenity
from rest_framework import status
from landlords.views import UserAuth
from landlords.models import Landlord
from rest_framework.views import APIView
from .serializers import AmenitySerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class ListView(APIView):
    def get(self, request):
        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data)
    
class CreateView(APIView):
    def post(self, request, property_pk):
        landlord = UserAuth.get(self, request)
        
        data = request.data.copy()
        data['property'] = property_pk
        
        serializer = AmenitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
