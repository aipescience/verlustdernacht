from django.db import models


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
    mjd = models.IntegerField()
    location = models.ForeignKey(Location)

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


class MoonPosition(models.Model):

    timestamp = models.DateTimeField()
    altitude = models.FloatField()
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.timestamp.isoformat()
