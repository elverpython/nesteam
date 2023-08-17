from django.http import JsonResponse
from rest_framework.generics import ListAPIView, \
    CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from .models import *
from .serializers import *
from .filters import GameFilter
from .models import Game

# def games_list(request):
#     game_lst = Game.objects.all()
#     serializer = GameSerializer(game_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)


def studios_list(request):
    studio_lst = Studio.objects.all()
    serializer = StudioSerializer(studio_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)

class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class StudiosCreateAPIView(CreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

class GamesView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameListAPIView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filterset_class = GameFilter

def game_info(request, pk):
    game_object = Game.objects.get(pk=pk)
    serializer = GameSerializer(game_object)
    return JsonResponse(serializer.data, safe=False)

class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

def genre_info(request, pk):
    genre_object = Genre.objects.get(pk=pk)
    serializer = GenreSerializer(genre_object)
    return JsonResponse(serializer.data, safe=False)