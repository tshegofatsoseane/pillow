from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    
    # Basic information
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    
    # Address
    street_address = models.CharField(max_length=255, null=True, blank=True)
    
    # Other
    institution = models.CharField(max_length=255, null=True, blank=True)
    
    # Metadata
    is_active = models.BooleanField(default=True)
    
    groups = models.ManyToManyField('auth.Group', related_name='student_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='student_permissions', blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []