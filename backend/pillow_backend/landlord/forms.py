from django import forms
from django.contrib.auth.models import AbstractUser
from .models import Landlord
from django.contrib.auth.forms import UserCreationForm


class LandlordRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = Landlord
        fields = ['username', 'email', 'password1', 'password2']
        
        
class LandlordUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=20)
    company_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
    
    class Meta:
        model = Landlord
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'company_name']