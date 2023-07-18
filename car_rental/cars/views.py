import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from car_rental.cars.models import Car
from car_rental.rental.forms import CarRentalForm

def index(request):
    cars = Car.objects.all()
    template_name = 'cars/index.html'
    form = CarRentalForm
    context = {
        'form': form, 
        'cars': cars
    }
    return render(request, template_name, context)