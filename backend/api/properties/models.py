from django.db import models
from .utils import geocode_address
from api.landlords.models import Landlord
from api.amenities.models import Amenity

# Create your models here.
class Property(models.Model):
    # Basic information
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    nearest_campus = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='properties')
    amenities = models.ManyToManyField(Amenity, blank=True)
    
    # Finances
    first_deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monthly_deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # More information
    description = models.TextField(blank=True, null=True)
    property_type = models.CharField(max_length=100, blank=True, null=True)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    available_rooms = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, default='available')
    pets_allowed = models.BooleanField(default=False)
    main_image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    virtual_tour_link = models.URLField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        location = geocode_address(self.street_address)
        if location:
            self.latitude = location['lat']
            self.longitude = location['lng']
        super(Property, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name