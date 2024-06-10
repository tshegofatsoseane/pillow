import os
import jwt
from .models import Property
from rest_framework import status
from django.shortcuts import render
from landlords.models import Landlord
from rest_framework.views import APIView
from .serializers import PropertySerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed


class UserAuth(APIView):
    """
    Authenticates the user based on the provided JWT token.

    Raises:
        AuthenticationFailed: If the token is missing, expired, or invalid.

    Returns:
        Landlord: The authenticated landlord object.
    """
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, os.environ['SECRET_KEY'], algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        landlord = Landlord.objects.filter(id=payload['id']).first()

        if not landlord:
            raise AuthenticationFailed('Invalid token')

        return landlord


class RegisterView(APIView):
    """
    Registers a new property.

    Args:
        request: The HTTP request object.

    Returns:
        Response: The HTTP response object.
    """
    def post(self, request):
        landlord = UserAuth.get(self, request)
        
        data = request.data.copy()
        data['landlord'] = landlord.id
        
        serializer = PropertySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class PropertyListView(APIView):
    """
    Retrieves a list of all properties.

    Args:
        request: The HTTP request object.

    Returns:
        Response: The HTTP response object containing the serialized property data.
    """
    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        
        return Response(serializer.data)
    

class PropertyUpdateView(APIView):
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
            property_instance = Property.objects.get(pk=pk, landlord=landlord)
            if not property_instance:
                return Response({'error': 'Permission denied'})
        except Property.DoesNotExist:
            return Response({
                "error": "Property not found",
                "details": "May not have permissions to update"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PropertySerializer(property_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class PropertyDeleteView(APIView):
    """
    Deletes a specific property.

    Args:
        request: The HTTP request object.
        pk: The primary key of the property to be deleted.

    Returns:
        Response: The HTTP response object.
    """
    def delete(self, request, pk):
        landlord = UserAuth.get(self, request)
        
        try:
            property_instance = Property.objects.filter(pk=pk, landlord=landlord)
            if not property_instance:
                return Response({'error': 'Permission denied'})
        except Exception as e:
            return Response({
                "error": e,
                "details": "May not have permissions to delete property"
            }, status=status.HTTP_404_NOT_FOUND)
            
        property_instance.delete()
        return Response({
            "message": "Property deleted successfully"
        }, status=status.HTTP_200_OK)