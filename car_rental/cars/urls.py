from django.urls import path, re_path
from car_rental.cars.views import *

app_name='cars'

urlpatterns = [
    path('', index, name='index'),
]