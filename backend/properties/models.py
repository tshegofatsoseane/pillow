from django.db import models
from landlords.models import Landlord

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    nearest_campus = models.CharField(max_length=255)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='properties')
    
    def __str__(self):
        return self.name