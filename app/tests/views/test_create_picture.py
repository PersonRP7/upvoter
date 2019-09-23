from .test_setup import TestSetup
from django.urls import reverse
# from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import tempfile
from app.models import Picture


class TestCreatePictureLoggedOut(TestSetup):

    def test_(self):
        response = self.client.get(
            reverse('app:create_picture')
        )
        self.assertRedirects(
            response,
            '/users/login/?next=/create_picture',
            status_code = 302,
            target_status_code = 200
        )

class TestCreatePictureLoggedIn(TestSetup):

    def setUp(self):
        super().setUp()
        self.client.login(
            username = "admin",
            password = "testing321"
        )

    def test_create_picture_get_200(self):
        response = self.client.get(
            reverse('app:create_picture')
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_create_picture_post(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix = '.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        response = self.client.post(
            reverse('app:create_picture'),
            {
                "user":self.user,
                "title":"Picture One",
                "cover":tmp_file
            },
            format = 'multipart'
        )
        self.assertRedirects(
            response,
            reverse('app:see_picture', kwargs = {'id':Picture.objects.first().id}),
            status_code = 302,
            target_status_code = 200
        )

