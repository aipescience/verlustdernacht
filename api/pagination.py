from collections import OrderedDict
from datetime import timedelta

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.pagination import BasePagination


class MeasurementPagination(BasePagination):
    display_page_controls = False

    def paginate_queryset(self, queryset, request, view=None):

        self.before = request.GET.get('before')
        if self.before:
            queryset = queryset.filter(timestamp__lt=self.before)

        self.after = request.GET.get('after')
        if not self.after:
            self.after = timezone.now() - timedelta(days=1)
        queryset = queryset.filter(timestamp__gt=self.after)

        self.every = request.GET.get('every')
        if self.every:
            queryset = queryset[::int(self.every)]

        return list(queryset)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', len(data)),
            ('every', self.every),
            ('before', self.before),
            ('after', self.after),
            ('results', data)
        ]))
