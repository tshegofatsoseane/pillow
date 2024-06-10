from django.db import models
from django.contrib.auth.models import AbstractUser


class Landlord(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []