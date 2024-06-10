import os
import jwt
import datetime
from .models import Landlord
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LandlordSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class UserAuth(APIView):
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
    def post(self, request):
        serializer = LandlordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        landlord = Landlord.objects.filter(email=email).first()
        
        if landlord is None:
            raise AuthenticationFailed('Landlord not found')
        
        if not landlord.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': landlord.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, os.environ['SECRET_KEY'], algorithm='HS256').decode('utf-8')
        
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "jwt": token
        }
        
        return response
    
    
class LandlordView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, os.environ['SECRET_KEY'], algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        landlord = Landlord.objects.filter(id=payload['id']).first()
        
        serializer = LandlordSerializer(landlord)
        
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        
        return response
    

class LandlordUpdateView(APIView):
    def put(self, request):
        landlord = UserAuth.get(self, request)
        
        try:
            landlord_instance = Landlord.objects.get(id=landlord.id)
            if not landlord_instance:
                return Response({'error': 'Permission denied'})
        except Landlord.DoesNotExist:
            return Response({
                "error": "Landlord not found",
                "details": "may not have permissions to update"
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = LandlordSerializer(landlord_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)