from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
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


class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = GameSerializer(data=data)
        if serializer.is_valid():
            game = Game()
            game.name = serializer.validated_data["name"]
            game.year = serializer.validated_data["year"]
            game.genre = serializer.validated_data["genre"]
            game.studio = serializer.validated_data["studio"]
            game.save()
            serializer = GameSerializer(instance=game)
            return Response(
                data=serializer.data,
                status=201
            )
        else:
            errors = serializer.error_messages
            response_data = {
                "message": "Данные не валидны",
                "errors": errors
            }
            return Response(
                data=response_data,
                status=400
            )


class GamesSearchView(APIView):
    def get(self, request):
        if 'key_word' in request.GET:
            key_word = request.GET['key_word']
        elif 'key_word' in request.data:
            key_word = request.data['key_word']
        else:
            return Response('no data', status=400)

        games = Game.objects.filter(
            Q(name__icontains=key_word) |
            Q(genre__name__icontains=key_word) |
            Q(studio__name__icontains=key_word)
        )

        serializer = GameSerializer(instance=games, many=True)
        json_data = serializer.data
        return Response(data=json_data)
def genre_info(request, pk):
    genre_object = Genre.objects.get(pk=pk)
    serializer = GenreSerializer(genre_object)
    return JsonResponse(serializer.data, safe=False)