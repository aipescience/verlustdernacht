from rest_framework import serializers

from .models import Location, Night, Measurement


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location


class NightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Night


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
