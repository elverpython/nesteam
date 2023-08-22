from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model



class AuthenticationTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword'
        )

    def test_authentication(self):
        url = reverse('token_create')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)