from django.urls import path
from car_rental.rental.views import *

app_name='rental'

urlpatterns = [
    path('', index, name='index'),
]