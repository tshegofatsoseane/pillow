from django.db import models
from .utils import geocode_address
from landlords.models import Landlord

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    nearest_campus = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='properties')
    
    def save(self, *args, **kwargs):
        location = geocode_address(self.street_address)
        if location:
            self.latitude = location['lat']
            self.longitude = location['lng']
        super(Property, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name