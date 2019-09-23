from django.test import TestCase
from users import forms

class TestCaptchaCorrect(TestCase):

    def test_captcha(self):
        data = {
            'captcha':'No'
        }
        form = forms.CaptchaMixin(data)
        self.assertTrue(
            form.is_valid()
        )

class TestCaptchaNotCorrect(TestCase):

    def setUp(self):
        self.cases = [
            {"captcha":"Yes"},
            {"captcha":"Maybe"},
            {"captcha":"Perhaps"}
        ]

    def test_wrong_captcha(self):
        for case in self.cases:
            form = forms.CaptchaMixin(
                case
            )
            self.assertFalse(
                form.is_valid()
            )
            # print(form['captcha'].errors.as_text())
            self.assertEqual(
                form['captcha'].errors.as_text(),
                "* You are a robot."
            )
