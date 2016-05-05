from django.contrib import admin

from .models import Location, Measurement


class LocationAdmin(admin.ModelAdmin):
    pass


class MeasurementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Measurement, MeasurementAdmin)
