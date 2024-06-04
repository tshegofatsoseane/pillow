from django import forms
from django.contrib.auth.models import AbstractUser
from .models import Landlord
from django.contrib.auth.forms import UserCreationForm


class LandlordRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = Landlord
        fields = ['username', 'email', 'password1', 'password2']