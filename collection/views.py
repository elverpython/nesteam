from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import GameCollection
from .serializers import CollectionSerializer
from .filters import CollectionFilter



class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer

class CollectionListAPIView(ListAPIView):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = CollectionFilter
