from django.db import models

class Accommodation(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    accreditation_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cell_number = models.CharField(max_length=20)
    street_address = models.CharField(max_length=255)
    nearest_campus = models.CharField(max_length=255)
    residence_name = models.CharField(max_length=255)
    university = models.CharField(max_length=50)
    
    latitude = models.FloatField(null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)
    image_url = models.URLField(max_length=255, null=True, blank=True)
    map_url = models.URLField(max_length=255, null=True, blank=True)
    directions_url = models.URLField(max_length=255, null=True, blank=True)  
    streetview_url = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.residence_name

    class Meta:
        db_table = 'Accommodations'
