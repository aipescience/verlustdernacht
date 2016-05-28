import math
from datetime import datetime

import ephem
from pytz import utc
from astropy.time import Time, TimeDelta
from astroplan import Observer

from .models import Location, Night, MoonPosition


def create_night(location_string, date_string):

    location = Location.objects.get(slug=location_string)

    if date_string:
        date = datetime.strptime(date_string, '%Y-%m-%d').replace(hour=12, minute=0, second=0, microsecond=0)
    else:
        date = datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)

    try:
        Night.objects.filter(location=location).get(date=date)
        print 'Night is already in the database.'
    except Night.DoesNotExist:

        time = Time(date)
        time_delta = TimeDelta(60000.0, format='sec')

        # guess if the moon is waxing or waning
        if ephem.next_full_moon(date) - ephem.Date(date) < ephem.Date(date) - ephem.previous_full_moon(date):
            waxing_moon = True
        else:
            waxing_moon = False

        observer = Observer(
            longitude=location.longitude,
            latitude=location.latitude,
            timezone='UTC'
        )

        moon_phase = observer.moon_phase(time).value

        if waxing_moon:
            moon_phase = (math.pi - moon_phase) / (2 * math.pi)
        else:
            moon_phase = (math.pi + moon_phase) / (2 * math.pi)

        times = {
            'sunset': observer.sun_set_time(time, which='next'),
            'civil_dusk': observer.twilight_evening_civil(time, which='next'),
            'nautical_dusk': observer.twilight_evening_nautical(time, which='next'),
            'astronomical_dusk': observer.twilight_evening_astronomical(time, which='next'),
            'midnight': observer.midnight(time, which='next'),
            'astronomical_dawn': observer.twilight_morning_astronomical(time, which='next'),
            'nautical_dawn': observer.twilight_morning_nautical(time, which='next'),
            'civil_dawn': observer.twilight_morning_civil(time, which='next'),
            'sunrise': observer.sun_rise_time(time, which='next'),
        }

        night = Night(date=date, location=location)
        night.mjd = int(time.mjd) + 1
        night.moon_phase = moon_phase
        for key in times:
            if times[key].jd > 0:
                setattr(night, key, times[key].to_datetime(timezone=utc))
        night.save()

        # moon_positions = []
        # for i in xrange(144):
        #     moon_altitude = observer.moon_altaz(time).alt.degree

        #     moon_position = MoonPosition(
        #         timestamp=time.to_datetime(timezone=utc),
        #         altitude=moon_altitude,
        #         location=location
        #     )

        #     moon_positions.append(moon_position)
        #     time += time_delta

        # MoonPosition.objects.bulk_create(moon_positions)
