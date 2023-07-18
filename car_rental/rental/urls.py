from django.urls import path
from car_rental.rental.views import *

app_name='rental'

urlpatterns = [
    path('', index, name='index'),
    path('rental_modal/', rental_modal, name='rental_modal'),
]