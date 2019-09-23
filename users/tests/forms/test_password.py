from django.test import TestCase
from users import forms

class TestPasswordMixin(TestCase):

    def setUp(self):
        self.errors = [
            'Password has to be longer than 9 characters.',
            'Password has to include at least one number.',
            'Password cannot contain password.'
        ]

    def test_form_correct(self):
        data = {
            'password1':'testing321',
            'password2':'testing321'
        }
        form = forms.PasswordMixin(data)
        self.assertTrue(
            form.is_valid()
        )

    def test_form_incorrect_length(self):
        data = {
            'password1':'testing32',
            'password2':'testing321'
        }
        form = forms.PasswordMixin(data)
        self.assertFalse(
            form.is_valid()
        )
        self.assertEqual(
            form['password1'].errors.as_text(),
            "* Password has to be longer than 9 characters."
        )

    def test_form_includes_password(self):
        data = {
            'password1':'password'
        }
        form = forms.PasswordMixin(data)
        self.assertFalse(
            form.is_valid()
        )
        for error in self.errors:
            self.assertTrue(
                error in form['password1'].errors
            )

    def test_form_includes_password(self):
        data = {
            'password1':'Password'
        }
        form = forms.PasswordMixin(data)
        self.assertFalse(
            form.is_valid()
        )
        
    def test_passwords_no_match(self):
        data = {
            'password1':'testing321',
            'password2':'testing980'
        }
        form = forms.PasswordMixin(data)
        self.assertFalse(
            form.is_valid()
        )

        self.assertEqual(
            form.errors.as_text(),
            "* __all__\n  * Passwords don't match."
        )
