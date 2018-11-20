import math
from datetime import datetime, time

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import ephem
from pytz import utc
from astropy.time import Time, TimeDelta
from astroplan import Observer


class Location(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    device = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta():
        ordering = ('slug', )

    def __str__(self):
        return self.name


class Night(models.Model):

    date = models.DateField(db_index=True)
    mjd = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    moon_phase = models.FloatField(null=True, blank=True)

    sunset = models.DateTimeField(null=True, blank=True)
    sunrise = models.DateTimeField(null=True, blank=True)
    midnight = models.DateTimeField(null=True, blank=True)

    civil_dusk = models.DateTimeField(null=True, blank=True)
    civil_dawn = models.DateTimeField(null=True, blank=True)
    nautical_dusk = models.DateTimeField(null=True, blank=True)
    nautical_dawn = models.DateTimeField(null=True, blank=True)
    astronomical_dusk = models.DateTimeField(null=True, blank=True)
    astronomical_dawn = models.DateTimeField(null=True, blank=True)

    class Meta():
        ordering = ('date', 'location')

    def __str__(self):
        return str(self.location) + ' ' + str(self.date)


@receiver(post_save, sender=Night)
def post_save_night(sender, **kwargs):
    if not kwargs.get('raw', False):
        night = kwargs['instance']

        location = night.location
        astropy_time = Time(datetime.combine(night.date, time(12)))
        astropy_time_delta = TimeDelta(600.0, format='sec')

        # guess if the moon is waxing or waning
        if ephem.next_full_moon(night.date) - ephem.Date(night.date) < ephem.Date(night.date) - ephem.previous_full_moon(night.date):
            waxing_moon = True
        else:
            waxing_moon = False

        observer = Observer(
            longitude=location.longitude,
            latitude=location.latitude,
            timezone='UTC'
        )

        moon_phase = observer.moon_phase(astropy_time).value

        if waxing_moon:
            moon_phase = (math.pi - moon_phase) / (2 * math.pi)
        else:
            moon_phase = (math.pi + moon_phase) / (2 * math.pi)

        times = {
            'sunset': observer.sun_set_time(astropy_time, which='next'),
            'civil_dusk': observer.twilight_evening_civil(astropy_time, which='next'),
            'nautical_dusk': observer.twilight_evening_nautical(astropy_time, which='next'),
            'astronomical_dusk': observer.twilight_evening_astronomical(astropy_time, which='next'),
            'midnight': observer.midnight(astropy_time, which='next'),
            'astronomical_dawn': observer.twilight_morning_astronomical(astropy_time, which='next'),
            'nautical_dawn': observer.twilight_morning_nautical(astropy_time, which='next'),
            'civil_dawn': observer.twilight_morning_civil(astropy_time, which='next'),
            'sunrise': observer.sun_rise_time(astropy_time, which='next'),
        }

        night.mjd = int(astropy_time.mjd) + 1
        night.moon_phase = moon_phase
        for key in times:
            if times[key].jd > 0:
                setattr(night, key, times[key].to_datetime(timezone=utc))

        post_save.disconnect(post_save_night, sender=sender)
        night.save()
        post_save.connect(post_save_night, sender=sender)

        moon_positions = []
        for i in range(144):
            moon_altitude = observer.moon_altaz(astropy_time).alt.degree

            moon_position = MoonPosition(
                timestamp=astropy_time.to_datetime(timezone=utc),
                altitude=moon_altitude,
                location=location
            )

            moon_positions.append(moon_position)
            astropy_time += astropy_time_delta

        MoonPosition.objects.bulk_create(moon_positions)


class Measurement(models.Model):

    timestamp = models.DateTimeField(db_index=True)
    magnitude = models.FloatField()
    frequency = models.IntegerField(null=True, blank=True)
    counts = models.IntegerField(null=True, blank=True)
    period = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta():
        ordering = ('timestamp', 'location')

    def __str__(self):
        return self.timestamp.isoformat()


class MoonPosition(models.Model):

    timestamp = models.DateTimeField(db_index=True)
    altitude = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta():
        ordering = ('timestamp', 'location')

    def __str__(self):
        return self.timestamp.isoformat()
