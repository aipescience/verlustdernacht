from django.db import models

from .utils import get_solar_values


class Location(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    device = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Night(models.Model):

    date = models.DateField()
    location = models.ForeignKey(Location)

    sunset = models.DateTimeField()
    sunrise = models.DateTimeField()
    nadir = models.DateTimeField()

    civil_dusk = models.DateTimeField()
    civil_dawn = models.DateTimeField()
    nautical_dusk = models.DateTimeField()
    nautical_dawn = models.DateTimeField()
    astronomical_dusk = models.DateTimeField()
    astronomical_dawn = models.DateTimeField()
    nadir = models.DateTimeField()

    def __str__(self):
        return str(self.location) + ' ' + str(self.date)


class Measurement(models.Model):

    timestamp = models.DateTimeField()
    magnitude = models.FloatField()
    frequency = models.IntegerField()
    counts = models.IntegerField()
    period = models.FloatField()
    temperature = models.FloatField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.timestamp.isoformat()
