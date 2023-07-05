from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import *
# Criar form para cadastro de carros na tela
# from .forms import *

def index(request):
    cars = Car.objects.all()
    template_name = 'cars/index.html'
    context = {
        'cars': cars
    }
    return render(request, template_name, context)