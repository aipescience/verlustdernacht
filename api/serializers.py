from rest_framework import serializers

from .models import Location, Measurement


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
