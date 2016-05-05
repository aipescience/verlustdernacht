from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Location, Measurement
from .serializers import MeasurementSerializer


class MeasurementViewSet(ReadOnlyModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    pagination_class = PageNumberPagination

    @list_route(methods=['get'])
    def latest(self, request):

        try:
            location = request.GET.get('location')
            if request.GET.get('location'):
                measurement = Measurement.objects.filter(location__slug=location).latest('timestamp')
            else:
                measurement = Measurement.objects.latest('timestamp')
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
