from django.contrib import messages
from django.contrib.auth import logout
from .forms import LandlordRegisterForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required


def register(request):
    """Registers a landlord onto the database"""
    if request.method == 'POST':
        form = LandlordRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account successfull created!')
            return redirect('landlord-login')
    else:
        form = LandlordRegisterForm()
    return render(request, 'landlord/register.html', {'form': form})

def logout_views(request):
    """Logs out the Landlord"""
    if request.method == 'POST':
        logout(request)
        return render(request, 'landlord/logout.html')
    else:
        return HttpResponseNotAllowed(['POST'])
