from django.test import TestCase
from django.urls import reverse
from app.models import Picture
from django.contrib.auth.models import User
from io import StringIO
from PIL import Image
from django.core.files.base import File

class TestSetUpClass(TestCase):

    @staticmethod
    def create_user():
        User.objects.create_user(
            username = "user",
            password = "testing321"
        )

    @staticmethod
    def create_picture(user, title):
        Picture.objects.create(
            user = user,
            title = title,
            cover = File(file=b"")
        )

    def setUp(self):
        TestSetUpClass.create_user()
        TestSetUpClass.create_picture(
            user = User.objects.get(username = "user"),
            title = "Picture One"
        )
        ############################3
        self.user = User.objects.get(
            username = 'user'
        )
        self.picture = Picture.objects.get(
            title = "Picture One"
        )