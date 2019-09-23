from django.test import TestCase
from django.urls import reverse
from app.models import Picture
from django.contrib.auth.models import User
from io import StringIO
from PIL import Image
from django.core.files.base import File

class SetUpClass(TestCase):
        
    @staticmethod
    def create_user():
        User.objects.create_user(
            username = "admin",
            password = "testing321"
        )

    def setUp(self):
        self.create_user()

class TestUpvote(SetUpClass):

    def setUp(self):
        super().setUp()
        self.user = User.objects.get(
            username = "admin"
        )
        Picture.objects.create(
            user = self.user,
            title = "Picture One",
            cover = File(file=b"")
        )

    def test_user_exists(self):
        self.assertTrue(
            self.user
        )

    def test_picture_exists(self):
        self.assertTrue(
            Picture.objects.get(
                title = "Picture One"
            )
        )



    

    