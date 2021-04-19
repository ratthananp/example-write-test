from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APITestCase

from main.apps.common.utils import merge_url_query_params
from main.apps.profiles.models import Profile


class ProfileTest(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make(User)
        self.client.force_login(self.user)
        self.url = reverse('backend:profile-list')

    def test_create_profile(self):
        data = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'role': 1,
            'username': 'test',
            'password': '12345',
            'email': 'test@example.com'
        }
        response = self.client.post(
            path=self.url,
            data=data
        )

        self.assertEqual(response.status_code, 201)  # can create profile and user

    def test_update_profile(self):
        profile = baker.make(Profile, user=baker.make(User))

        data = {
            'first_name': 'test'
        }

        response = self.client.patch(
            path=self.url + f'{profile.id}/',
            data=data
        )

        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(
            response_json['first_name'],
            'test'
        )  # first name changed

        self.assertEqual(
            response_json['updated_user'],
            self.user.id
        )  # updated user changed

    def test_delete_profile(self):
        profile = baker.make(Profile, user=baker.make(User))
        response = self.client.delete(
            path=self.url + f'{profile.id}/',
        )
        self.assertEqual(response.status_code, 204)  # can delete profile

    def test_list_profile(self):

        # create multiple profiles
        for _ in range(10):
            baker.make(Profile, user=baker.make(User))

        # normal list
        response = self.client.get(
            path=self.url,
        )
        self.assertEqual(response.status_code, 200)

        # django restql https://github.com/yezyilomo/django-restql
        query_params = {
            "query": "{id, first_name}"
        }
        url = merge_url_query_params(self.url, query_params)
        response = self.client.get(
            path=url,
        )
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(
            len(response_json['results'][0]),
            2
        )
