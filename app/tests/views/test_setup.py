from django.test import TestCase
from app.models import User, Picture
from PIL import Image
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile



class TestSetup(TestCase):

    def create_image(self):
        testfile = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
            )
        picture = SimpleUploadedFile('picture.gif', testfile, content_type = 'image/gif')
        Picture.objects.create(
            user = self.user,
            title = "Picture One",
            cover = picture
        )
        

    def setUp(self):
        self.user = User.objects.create_user(
            username = "admin",
            email = "admin@email.com",
            password = "testing321"
        )
