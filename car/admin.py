from django.contrib import admin
from .models import Cartype,Carvarient,CarEngineandTransmission,Comfort,Fuel,Exterior,Brand,Car

# Register your models here.
admin.site.register(Cartype)
admin.site.register(Carvarient)
admin.site.register(CarEngineandTransmission)
admin.site.register(Comfort)
admin.site.register(Fuel)
admin.site.register(Exterior)
admin.site.register(Brand)
admin.site.register(Car)