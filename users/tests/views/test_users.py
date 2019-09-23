from django.test import TestCase
from django.urls import reverse

class TestOne(TestCase):

    def test_users(self):
        response = self.client.get(
            reverse('users:users')
        )
        self.assertEqual(
            response.status_code,
            200
        )