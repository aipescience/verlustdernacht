from __future__ import unicode_literals

from django.db import models


class Location(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


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
