from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission

# Create your models here.
class Landlord(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=120)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='landlord_profiles/',
                                        blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # other fields
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="landlord_groups",
        related_query_name="landlord",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="landlord_user_permissions",
        related_query_name="landlord",
    )
    
    def __str__(self):
        return self.username