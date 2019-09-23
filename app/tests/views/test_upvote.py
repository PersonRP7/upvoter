from .test_setup import TestSetup
from django.urls import reverse
from app.models import Picture, Upvote, Downvote
import unittest


class TestUpvoteLoggedOut(TestSetup):

    def setUp(self):
        super().setUp()
        self.create_image()

    def test_upvote_get(self):
        response = self.client.get(
            reverse(
                'app:upvote',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.status_code,
            405
        )

    # @unittest.expectedFailure
    # def test_upvote_post(self):
    #     response = self.client.post(
    #         reverse(
    #             'app:upvote',
    #             kwargs = {'id':Picture.objects.first().id}
    #         )
    #     )
    #     print(response)
    #     self.assertTrue(1)
    def test_upvote_post(self):
        response = self.client.post(
            reverse(
                'app:upvote',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.status_code,
            401
        )

class TestUpvote(TestSetup):

    def setUp(self):
        super().setUp()
        self.create_image()
        self.client.login(
            username = "admin",
            password = "testing321"
        )

    def test_upvote_get(self):
        response = self.client.get(
            reverse(
                'app:upvote',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.status_code,
            405
        )

    def test_upvote_post(self):
        response = self.client.post(
            reverse(
                'app:upvote',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            Upvote.objects.count(),
            1
        )
        self.assertEqual(
            Downvote.objects.count(),
            0
        )


