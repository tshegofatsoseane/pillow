from django.db import models
from api.students.models import Student
from api.properties.models import Property


class Review(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review by {self.user.email} for {self.property.name}'