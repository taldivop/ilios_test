from django.contrib import admin
from car_rental.rental.models import Rental


class RentalAdmin(admin.ModelAdmin):

    list_display = ['car', 'pick_up_date', 'drop_off_date', 'created_at']
    search_fields = ['pick_up_date', 'drop_off_date']

admin.site.register(Rental, RentalAdmin)
