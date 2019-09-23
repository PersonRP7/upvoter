from django.test import TestCase
from users import forms
from django.contrib.auth.models import User

class TestEmailMixinCorrect(TestCase):

    def test_email_mixin(self):
        data = {
            'email':'user@email.com'
        }
        form = forms.EmailMixin(data)
        self.assertTrue(
            form.is_valid()
        )


class TestEmailMixinIncorrect(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = "user",
            password = "testing321",
            email = "user@email.com"
        )

    def test_email_mixin_error(self):
        data = {
            'email':'user@email.com'
        }
        form = forms.EmailMixin(data)
        self.assertFalse(
            form.is_valid()
        )
        self.assertEqual(
            form['email'].errors.as_text(),
            "* user@email.com is taken."
        )
