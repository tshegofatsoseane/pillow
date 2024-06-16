import os
import jwt
from .models import Review
from rest_framework import status
from django.shortcuts import render
from api.students.models import Student
from rest_framework.views import APIView
from api.landlords.models import Landlord
from .serializers import ReviewSerializer
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


class CreateReview(APIView):
    """
    Registers a new review.

    Args:
        request: The HTTP request object.

    Returns:
        Response: The HTTP response object.
    """
    def post(self, request):
        student = UserAuth.get(self, request)
        
        data = request.data.copy()
        data['user'] = student.id
        
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ListReview(APIView):
    """
    Retrieves a list of all reviews.

    Args:
        request: The HTTP request object.

    Returns:
        Response: The HTTP response object containing the serialized review data.
    """
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
    

class ReviewUpdateView(APIView):
    """
    Updates a specific review.

    Args:
        request: The HTTP request object.
        pk: The primary key of the review to be updated.

    Returns:
        Response: The HTTP response object.
    """
    def put(self, request, pk):
        student = UserAuth.get(self, request)
        
        try:
            review_instance = Review.objects.get(pk=pk, user=student)
            if not review_instance:
                return Response({'error': 'Permission denied'})
        except Review.DoesNotExist:
            return Response({
                "error": "Property not found",
                "details": "May not have permissions to update"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReviewSerializer(review_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ReviewDeleteView(APIView):
    """
    Deletes a specific review.

    Args:
        request: The HTTP request object.
        pk: The primary key of the review to be deleted.

    Returns:
        Response: The HTTP response object.
    """
    def delete(self, request, pk):
        student = UserAuth.get(self, request)
        
        try:
            review_instance = Review.objects.filter(pk=pk, user=student)
            if not review_instance:
                return Response({'error': 'Permission denied'})
        except Exception as e:
            return Response({
                "error": e,
                "details": "May not have permissions to delete review"
            }, status=status.HTTP_404_NOT_FOUND)
            
        review_instance.delete()
        return Response({
            "message": "Property deleted successfully"
        }, status=status.HTTP_200_OK)