import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from car_rental.cars.models import Car
from car_rental.rental.forms import CarRentalForm

def index(request):
    cars = Car.objects.all()
    template_name = 'cars/index.html'
    form = CarRentalForm
    context = {}
    if request.method == 'POST':
        form = CarRentalForm(request.POST or None)
        if form.is_valid():
            pick_up_date = form.cleaned_data['pick_up_date']
            drop_off_date = form.cleaned_data['drop_off_date']
            
            if pick_up_date.date() < datetime.date.today():
                form.add_error('pick_up_date', 'A data de retirada não pode ser anterior ao dia de hoje.')
            
            if drop_off_date < pick_up_date:
                form.add_error('drop_off_date', 'A data de devolução deve ser maior do que a data de retirada.')
            
            if not form.errors:
                form.save()
                context['success'] = True
    else:
        form = CarRentalForm()
    context['form'] = form
    context['cars'] = cars
    return render(request, template_name, context)