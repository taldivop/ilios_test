from django.contrib import admin
from .models import *


class RentalAdmin(admin.ModelAdmin):

    list_display = ['car', 'pick_up_date', 'drop_off_date', 'created_at']
    search_fields = ['pick_up_date', 'drop_off_date']

admin.site.register(Rental, RentalAdmin)
