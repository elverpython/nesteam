from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django_filters import rest_framework as filters
from .models import GameCollection
import  django_filters


class CollectionFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    author__gt = django_filters.NumberFilter(field_name='author', lookup_expr='gt')
    author__lt = django_filters.NumberFilter(field_name='author', lookup_expr='lt')

    class Meta:
        model = GameCollection
        fields = ['name']