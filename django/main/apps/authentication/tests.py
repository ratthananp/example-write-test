from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.profiles.models import Profile


class AuthenticationTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('backend:token-auth')
        self.user = baker.make(
            User,
            username='test',
        )
        self.user.set_password('12345')
        self.user.save()

        self.profile = baker.make(
            Profile,
            user=self.user
        )

        self.client.force_login(self.user)

    def test_token_auth(self):
        data = {
            'username': 'test',
            'password': '12345'
        }
        response = self.client.post(
            path=self.url,
            data=data
        )
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('refresh' in response_json)
        self.assertTrue('access' in response_json)
