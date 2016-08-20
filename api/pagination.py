from collections import OrderedDict
from datetime import timedelta

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.pagination import BasePagination


class AbstractPagination(BasePagination):
    display_page_controls = False

    def paginate_queryset(self, queryset, request, view=None):

        queryset = self.filter_location(queryset, request)
        queryset = self.filter_before(queryset, request)
        queryset = self.filter_after(queryset, request)
        queryset = self.filter_every(queryset, request)

        return list(queryset)

    def filter_location(self, queryset, request):
        location = request.GET.get('location')
        if location:
            queryset = queryset.filter(location__slug=location)
        return queryset

    def filter_before(self, queryset, request):
        self.before = request.GET.get('before')
        if self.before:
            queryset = queryset.filter(timestamp__lt=self.before)
        return queryset

    def filter_after(self, queryset, request):
        self.after = request.GET.get('after')
        if not self.after:
            self.after = timezone.now() - timedelta(days=1)
        queryset = queryset.filter(timestamp__gt=self.after)
        return queryset

    def filter_every(self, queryset, request):
        self.every = request.GET.get('every')
        if self.every:
            queryset = queryset[::int(self.every)]
        return queryset


class MeasurementPagination(AbstractPagination):

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', len(data)),
            ('every', self.every),
            ('before', self.before),
            ('after', self.after),
            ('measurements', data)
        ]))


class MoonPositionPagination(AbstractPagination):

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', len(data)),
            ('every', self.every),
            ('before', self.before),
            ('after', self.after),
            ('moonpositions', data)
        ]))


class NightPagination(AbstractPagination):

    def filter_before(self, queryset, request):
        self.before = request.GET.get('before')
        if self.before:
            queryset = queryset.filter(date__lte=self.before)
        return queryset

    def filter_after(self, queryset, request):
        self.after = request.GET.get('after')
        if self.after:
            queryset = queryset.filter(date__gte=self.after)
        return queryset

    def filter_every(self, queryset, request):
        return queryset

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', len(data)),
            ('before', self.before),
            ('after', self.after),
            ('nights', data)
        ]))
