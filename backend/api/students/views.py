import os
import jwt
import datetime
from .models import Student
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class UserAuth(APIView):
    """
    This class handles user authentication for the API view.
    """

    def get(self, request):
        """
        Handles the GET request for user authentication.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Landlord: The authenticated landlord object.

        Raises:
            AuthenticationFailed: If the request is unauthenticated or the token is invalid.
        """
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, os.environ['SECRET_KEY'], algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        student = Student.objects.filter(id=payload['id']).first()

        if not student:
            raise AuthenticationFailed('Invalid token')

        return student


class RegisterView(APIView):
    """
    This class handles the registration of a new Student.
    """

    def post(self, request):
        """
        Handles the POST request for Student registration.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The serialized Student data.

        Raises:
            ValidationError: If the request data is invalid.
        """
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    """
    This class handles user login and token generation.
    """

    def post(self, request):
        """
        Handles the POST request for user login.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The token for authentication.

        Raises:
            AuthenticationFailed: If the email or password is incorrect.
        """
        email = request.data['email']
        password = request.data['password']

        student = Student.objects.filter(email=email).first()

        if student is None:
            raise AuthenticationFailed('Student not found')

        if not student.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': student.id,
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


class StudentView(APIView):
    """
    This class handles the retrieval of Student data.
    """

    def get(self, request):
        """
        Handles the GET request for Student data.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The serialized Student data.

        Raises:
            AuthenticationFailed: If the request is unauthenticated or the token is invalid.
        """
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, os.environ['SECRET_KEY'], algorithm='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        student = Student.objects.filter(id=payload['id']).first()

        serializer = StudentSerializer(student)

        return Response(serializer.data)


class LogoutView(APIView):
    """
    This class handles user logout and token deletion.
    """

    def post(self, request):
        """
        Handles the POST request for user logout.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: A success message.

        """
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response


class StudentUpdateView(APIView):
    """
    This class handles the update of Student data.
    """

    def put(self, request):
        """
        Handles the PUT request for updating Student data.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The updated serialized Student data.

        Raises:
            AuthenticationFailed: If the request is unauthenticated or the token is invalid.
            NotFound: If the Student is not found.
            ValidationError: If the request data is invalid.
        """
        student = UserAuth.get(self, request)

        try:
            student_instance = student.objects.get(id=student.id)
            if not student_instance:
                return Response({'error': 'Permission denied'})
        except Student.DoesNotExist:
            return Response({
                "error": "Student not found",
                "details": "may not have permissions to update"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)