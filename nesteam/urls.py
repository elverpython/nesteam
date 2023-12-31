"""
URL configuration for nesteam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from games.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('games/', games_list, name='games'),
    # path('studios/', studios_list, name='studios'),
    path('games/', GamesView.as_view(), name='games'),
    path('games-search/', GamesSearchView.as_view(), name='games-search'),
    path('gamefilter/', GameListAPIView.as_view(), name='gamefilter'),
    path('game-detail/<int:pk>/', game_info, name='games-info'),
    path('genre-detail/<int:pk>/', genre_info, name='genre-info'),
    path('studios/', StudiosListAPIView.as_view(), name='games'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('create-studios/', StudiosCreateAPIView.as_view(), name='create-studios'),
    # path('users/', users_list, name='users'),
    path('users/', include('usersapp.urls')),
    path('collections/', include('collection.urls')),
    path('', include(router.urls)),

]

