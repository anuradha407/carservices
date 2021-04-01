from django.contrib import admin
from .models import Car
# Register your models here.

admin.site.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model','car-notes','car_number','year_old','service_type']
