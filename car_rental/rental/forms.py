from django import forms

from car_rental.rental.models import Rental


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class CarRentalForm(forms.ModelForm):

    class Meta:
        model = Rental
        fields = '__all__'
        widgets = {
            'pick_up_date': DateTimeInput(),
            'drop_off_date': DateTimeInput(),
        }

    

