from django.shortcuts import render

from .models import *


def index(request):
    rentals = Rental.objects.all()
    template_name = 'rental/index.html'
    context = {
        'rentals': rentals,
    }
    return render(request, template_name, context)

# Create your views here.
