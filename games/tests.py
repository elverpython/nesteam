
from rest_framework.test import APITestCase
from .factories import GameFactory, GenreFactory

class GamesTest(APITestCase):
    def setUp(self):
        self.game_1 = GameFactory()
        self.game_2 = GameFactory()
        self.genre = GenreFactory()

    def test_get_list_of_games(self):
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, 200)


    def test_get_one_game(self):
        response = self.client.get(f'/game-detail/{self.game_1.pk}/')
        self.assertEqual(response.status_code, 200)


    def test_get_genre(self):
        response = self.client.get(f'/genre-detail/{self.genre.pk}/')
        self.assertEqual(response.status_code, 200)