from django_filters import rest_framework as filters
from .models import Game
import  django_filters


class GameFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    year__gt = django_filters.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = django_filters.NumberFilter(field_name='year', lookup_expr='lt')

    class Meta:


        model = Game
        fields = ['name']