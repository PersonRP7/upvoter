from .test_setup import TestSetup
from app.models import User, Picture
from app.helpers import seek_instance
from django.urls import reverse
from django.core.files.base import File

class TestSeekInstance(TestSetup):

    def test_previous(self):
        value = seek_instance(
            self.picture2, "lt", "-pk"
        )
        self.assertEqual(
            value,
            f"/see_picture/{self.picture1.id}/"
        )

    def test_next(self):
        value = seek_instance(
            self.picture1, "gt", "pk"
        )
        self.assertEqual(
            value,
            f"/see_picture/{self.picture2.id}/"
        )

