from django.urls import path
from car_rental.core.views import *

app_name='core'

urlpatterns = [
    path('', home, name='home'),
]