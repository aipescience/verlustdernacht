from django.contrib import admin

from .models import *


class NightAdmin(admin.ModelAdmin):
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


admin.site.register(Location)
admin.site.register(Night, NightAdmin)
admin.site.register(Measurement)
admin.site.register(MoonPosition)
