from django.test import TestCase
from users import forms
from django.contrib.auth.models import User

class TestUsernameMixinCorrect(TestCase):

    def test_username(self):
        data = {
            'username':'user'
        }
        form = forms.UsernameMixin(data)
        self.assertTrue(
            form.is_valid()
        )

class TestUsernameMixinNotCorrect(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = "user",
            password = "testing321"
        )

    def test_username_incorrect(self):
        data = {
            'username':'user'
        }
        form = forms.UsernameMixin(data)
        self.assertFalse(
            form.is_valid()
        )
        self.assertEqual(
            form['username'].errors.as_text(),
            "* user is taken."
        )