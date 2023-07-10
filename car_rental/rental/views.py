from django.shortcuts import render

from .models import *


def index(request):
    rental = Rental.objects.all()
    template_name = 'rental/index.html'
    context = {
        'rental': rental,
    }
    return render(request, template_name, context)

# Create your views here.
