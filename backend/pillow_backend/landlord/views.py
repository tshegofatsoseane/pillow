from django.shortcuts import render, redirect
from .forms import LandlordRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = LandlordRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account successfull created!')
            return redirect('/')
    else:
        form = LandlordRegisterForm()
    return render(request, 'landlord/register.html', {'form': form})