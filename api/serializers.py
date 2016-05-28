from rest_framework import serializers

from .models import *


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location


class NightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Night


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('id', 'timestamp', 'magnitude')


class MoonPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoonPosition
        fields = ('id', 'timestamp', 'altitude')
