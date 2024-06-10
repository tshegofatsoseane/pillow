from django.db import models
from properties.models import Property


class Amenity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenities', null=True, blank=True)
    
    def __str__(self):
        return self.name