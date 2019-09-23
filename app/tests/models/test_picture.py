from .test_setup import TestSetUpClass
from app.models import Picture

class TestPicture(TestSetUpClass):

    def setUp(self):
        super().setUp()
        # self.picture = Picture.objects.get(
        #     title = "Picture One"
        # )

    def test_picture(self):
        self.assertTrue(
            self.picture
        )