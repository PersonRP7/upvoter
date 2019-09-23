from django.test import TestCase
from users import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class TestCaptcha(TestCase):

    def test_captcha_error(self):
        with self.assertRaises(ValidationError):
            validators.validate_captcha("yes")


class TestPasswordLength(TestCase):

    def test_password_length(self):
        with self.assertRaises(ValidationError):
            validators.validate_password_length(
                "qwertyuio"
            )

class TestPasswordIncludesNumber(TestCase):

    def test_password_number(self):
        with self.assertRaises(ValidationError):
            validators.validate_password_number(
                "qwertyu"
            )

class TestPasswordIncludesPassword(TestCase):

    def test_password_password(self):
        words = ['password', 'Password']
        for word in words:
            with self.assertRaises(ValidationError):
                validators.validate_password_password(word)

class TestUsernameValidator(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = "user",
            password = "testing321"
        )

    def test_username(self):
        with self.assertRaises(ValidationError):
            validators.validate_username(self.user.username)
  
class TestEmailValidator(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = "user",
            email = "email@email.com",
            password = "testing321"
        )

    def test_email(self):
        with self.assertRaises(ValidationError):
            validators.validate_email(self.user.email)