import dateutil.parser

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import *
from .serializers import *
from .pagination import *


class LocationViewSet(ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class NightViewSet(ReadOnlyModelViewSet):
    serializer_class = NightSerializer
    pagination_class = NightPagination

    def get_queryset(self):
        queryset = Night.objects.all()

        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(date=dateutil.parser.parse(date).date())

        return queryset

    @list_route(methods=['get'])
    def latest(self, request):
        location_slug = request.GET.get('location')
        if location_slug:
            try:
                location = Location.objects.get(slug=location_slug)
            except Location.DoesNotExist:
                location = None
        else:
            location = None

        try:
            if location is None:
                night = Night.objects.latest('date')
            else:
                night = Night.objects.filter(location=location).latest('date')
        except Night.DoesNotExist:
            return Response('Error: No latest night could be found.', status=404)

        serializer = self.get_serializer(night)
        return Response([serializer.data])


class MeasurementViewSet(ReadOnlyModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    pagination_class = MeasurementPagination

    @list_route(methods=['get'])
    def latest(self, request):
        location_slug = request.GET.get('location')
        if location_slug:
            try:
                location = Location.objects.get(slug=location_slug)
            except Location.DoesNotExist:
                location = None
        else:
            location = None

        try:
            if location is None:
                measurement = Measurement.objects.latest('timestamp')
            else:
                measurement = Measurement.objects.filter(location=location).latest('timestamp')
        except Measurement.DoesNotExist:
            return Response('Error: No latest measurement could be found.', status=404)

        serializer = self.get_serializer(measurement)
        return Response(serializer.data)

    @list_route(methods=['post'], permission_classes=[IsAuthenticated])
    def ingest(self, request):

        try:
            location = Location.objects.get(slug=request.data['location'])
        except:
            return Response('Error: The provided location was not found.', status=404)

        measurements = []
        for row in request.data['rows']:
            measurements.append(
                Measurement(
                    timestamp=row[1],
                    magnitude=row[2],
                    frequency=row[3],
                    counts=row[4],
                    period=row[5],
                    temperature=row[6],
                    location=location
                )
            )

        if len(measurements) == request.data['count']:
            Measurement.objects.bulk_create(measurements)
            return Response('Ok')
        else:
            return Response(status=500)


class MoonPositionViewSet(ReadOnlyModelViewSet):
    queryset = MoonPosition.objects.all()
    serializer_class = MoonPositionSerializer
    pagination_class = MoonPositionPagination
