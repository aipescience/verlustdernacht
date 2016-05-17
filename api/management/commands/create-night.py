from datetime import datetime, timedelta

from pytz import utc
from astropy.time import Time
from astroplan import Observer

from django.core.management.base import BaseCommand

from api.models import Location, Night


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('location', action='store', help='Location for this night')
        parser.add_argument('date', action='store', default=False, nargs='?', help='Date for this night')

    def handle(self, *args, **options):

        location = Location.objects.get(slug=options['location'])
        if options['date']:
            date = datetime.strptime(options['date'], '%Y-%m-%d').replace(hour=12, minute=0, second=0, microsecond=0)
        else:
            date = datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)

        location = Location.objects.get(slug=options['location'])

        astro_date = Time(date)

        observer = Observer(longitude=location.longitude, latitude=location.latitude, timezone='UTC')

        night = Night(date=date, location=location)

        night.sunset = observer.sun_set_time(astro_date, which='next').to_datetime(timezone=utc)
        night.civil_dusk = observer.twilight_evening_civil(astro_date, which='next').to_datetime(timezone=utc)
        night.nautical_dusk = observer.twilight_evening_nautical(astro_date, which='next').to_datetime(timezone=utc)
        #night.astronomical_dusk = observer.twilight_evening_astronomical(astro_date, which='next').to_datetime(timezone=utc)
        night.nadir = observer.midnight(astro_date, which='next').to_datetime(timezone=utc)
        #night.astronomical_dawn = observer.twilight_morning_astronomical(astro_date, which='next').to_datetime(timezone=utc)
        night.nautical_dawn = observer.twilight_morning_nautical(astro_date, which='next').to_datetime(timezone=utc)
        night.civil_dawn = observer.twilight_morning_civil(astro_date, which='next').to_datetime(timezone=utc)
        night.sunrise = observer.sun_rise_time(astro_date, which='next').to_datetime(timezone=utc)

        night.save()
