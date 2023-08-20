from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import Player
from .filters import PlayerFilter




def users_list(request):
    user_lst = User.objects.all()
    serializer = UserSerializer(user_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)


def user_info(request, pk):
    user_object = User.objects.get(pk=pk)
    serializer = UserListSerializer(user_object)
    return JsonResponse(serializer.data, safe=False)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filterset_class = PlayerFilter


    # def get(self, request):
    #     players = Player.objects.all()
    #     filter_backends = (filters.DjangoFilterBackend,)
    #     filterset_class = ProductFilter
    #     serializer = PlayerSerializer(instance=players, many=True)
    #     return Response(data=serializer.data)