from django.shortcuts import render, redirect
from car_rental.rental.forms import CarRentalForm
from django.contrib import messages
from django.http import JsonResponse

from .models import *


def index(request):
    rentals = Rental.objects.all()
    template_name = 'rental/index.html'
    context = {
        'rentals': rentals,
    }
    return render(request, template_name, context)


def rental_modal(request):
    template_name = 'rental/rental_modal.html'
    context = {}
    if request.method == 'POST':
        form = CarRentalForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua reserva foi feita com sucesso.')
            return redirect('cars:index')
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
                return redirect('cars:index')
    else:
        form = CarRentalForm()
    context['form'] = form
    return render(request, template_name, context)