from django.contrib import admin

from .models import *


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'device', 'latitude', 'longitude')

class NightAdmin(admin.ModelAdmin):
    search_fields = ('date', )
    list_display = ('date', 'mjd', 'location')
    list_filter = ('location', )

    readonly_fields = (
        'mjd',
        'moon_phase',
        'sunset',
        'sunrise',
        'midnight',
        'civil_dusk',
        'civil_dawn',
        'nautical_dusk',
        'nautical_dawn',
        'astronomical_dusk',
        'astronomical_dawn',
    )


class MeasurementAdmin(admin.ModelAdmin):
    search_fields = ('timestamp', )
    list_display = ('timestamp', 'location', 'magnitude', 'frequency', 'counts', 'period', 'temperature')
    list_filter = ('location', )


class MoonPositionAdmin(admin.ModelAdmin):
    search_fields = ('timestamp', )
    list_display = ('timestamp', 'altitude', 'location')
    list_filter = ('location', )

admin.site.register(Location, LocationAdmin)
admin.site.register(Night, NightAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(MoonPosition, MoonPositionAdmin)
