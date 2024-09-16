from django.contrib import admin
from .models import Accommodation

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('residence_name', 'accreditation_number', 'email', 'nearest_campus', 'university', 'latitude', 'longitude')
