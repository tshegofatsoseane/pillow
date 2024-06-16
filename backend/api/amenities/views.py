import os
import jwt
from .models import Amenity
from rest_framework import status
from api.landlords.views import UserAuth
from api.landlords.models import Landlord
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

class AmenityUpdateView(APIView):
    """
    Updates a specific property.

    Args:
        request: The HTTP request object.
        pk: The primary key of the property to be updated.

    Returns:
        Response: The HTTP response object.
    """
    def put(self, request, pk):
        landlord = UserAuth.get(self, request)
        
        try:
            property_instance = Amenity.objects.get(pk=pk)
            if not property_instance:
                return Response({'error': 'Permission denied'})
        except Amenity.DoesNotExist:
            return Response({
                "error": "Property not found",
                "details": "May not have permissions to update"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AmenitySerializer(property_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    