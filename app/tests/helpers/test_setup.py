from django.test import TransactionTestCase
from app.models import Picture, User
from django.core.files.base import File

class TestSetup(TransactionTestCase):

    def create_user(self):
        User.objects.create_user(
            username = "admin",
            password = "testing321"
        )

    def create_picture(self, title = None):
        Picture.objects.create(
            user = User.objects.get(username = "admin"),
            title = title,
            cover = File(file=b"")
        )

    pictures = ["Picture One", "Picture Two"]
    
    def setUp(self):
        self.create_user()
        for picture in self.pictures:
            self.create_picture(title = picture)
        self.user = User.objects.get(
            username = "admin"
        )
        self.picture1 = Picture.objects.get(
            title = "Picture One"
        )
        self.picture2 = Picture.objects.get(
            title = "Picture Two"
        )



