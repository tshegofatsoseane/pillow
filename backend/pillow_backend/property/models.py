from django.db import models
from landlord.models import Landlord
from django.contrib.auth import get_user_model


class Property(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name