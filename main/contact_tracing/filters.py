import django_filters
from .models import *


class StatFilter(django_filters.FilterSet):
    # date = django_filters.DateFromToRangeFilter()
    # time = django_filters.TimeRangeFilter()

    class Meta:
        model = Stat
        fields = ['room']


class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = ['building']


class LogFilter(django_filters.FilterSet):
    class Meta:
        model: Log
        fields = ['time_created']

