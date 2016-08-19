from datetime import datetime

from .models import Location, Night


def create_night(location_string, date_string):

    location = Location.objects.get(slug=location_string)

    if date_string:
        date = datetime.strptime(date_string, '%Y-%m-%d').replace(hour=12, minute=0, second=0, microsecond=0)
    else:
        date = datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)

    Night.objects.get_or_create(location=location, date=date)
