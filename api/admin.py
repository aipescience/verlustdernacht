from django.contrib import admin

from .models import *


admin.site.register(Location)
admin.site.register(Night)
admin.site.register(Measurement)
admin.site.register(MoonPosition)
