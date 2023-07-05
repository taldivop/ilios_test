from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):

    list_display = ['model', 'plate', 'slug', 'year', 'created_at']
    search_fields = ['model', 'slug']
    prepopulated_fields = {'slug': ('model', 'plate')}

admin.site.register(Car, CarAdmin)
