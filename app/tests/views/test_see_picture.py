from .test_setup import TestSetup
from django.urls import reverse
from app.models import Picture, Upvote, Downvote

class TestSeePictureNotLoggedIn(TestSetup):

    def setUp(self):
        super().setUp()
        self.create_image()

    def test_see_picture_get(self):
        response = self.client.get(
            reverse(
                'app:see_picture',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )

class TestSeePictureLoggedIn(TestSetup):

    def setUp(self):
        super().setUp()
        self.create_image()
        self.client.login(
            username = "admin",
            password = "testing321"
        )

    def test_see_picture_get(self):
        response = self.client.get(
            reverse(
                'app:see_picture',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.status_code,
            200
        )

class TestViewRendersContext(TestSetup):

    def setUp(self):
        super().setUp()
        self.create_image()
        self.picture = Picture.objects.get(
            user = self.user
        )
        Upvote.objects.create(
            user = self.user,
            picture = self.picture
        )

    def test_template_renders(self):
        response = self.client.get(
            reverse(
                'app:see_picture',
                kwargs = {'id':Picture.objects.first().id}
            )
        )
        self.assertEqual(
            response.context['upvote_count'],
            1
        )
        self.assertEqual(
            response.context['downvote_count'],
            0
        )


