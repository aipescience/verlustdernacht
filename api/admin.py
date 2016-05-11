from django.contrib import admin

from .models import Location, Night, Measurement


admin.site.register(Location)
admin.site.register(Night)
admin.site.register(Measurement)
