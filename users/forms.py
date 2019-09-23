from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .validators import validate_captcha, validate_password_length, validate_password_password
from .validators import validate_password_number, validate_username, validate_email

class CaptchaMixin(forms.Form):
    Yes = 'Yes'
    No = 'No'
    Maybe = 'Maybe'
    Perhaps = 'Perhaps'
    CAPTCHA_BOOLEANS = (
        (Yes, 'Yes'),
        (Maybe, 'Maybe'),
        (No, 'No'),
        (Perhaps, 'Perhaps')
    )

    captcha = forms.ChoiceField(choices = CAPTCHA_BOOLEANS,
    label = "Are you a robot?", validators = [validate_captcha])

class EmailMixin(forms.Form):
    email = forms.EmailField(
        validators = [validate_email]
    )

class UsernameMixin(forms.Form):
    username = forms.CharField(
        validators = [validate_username]
    )

class PasswordMixin(forms.Form):
    password1 = forms.CharField(
        widget = forms.PasswordInput(),
        max_length = 50,
        validators = [
            validate_password_length,
            validate_password_number,
            validate_password_password
        ]
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(),
        max_length = 50
    )

    def clean(self):
        data = self.cleaned_data
        if 'password1' in data and 'password2' in data \
        and data['password1'] != data['password2']:
            raise ValidationError(
                "Passwords don't match."
            )

class UserRegisterCaptchaForm(CaptchaMixin, PasswordMixin, EmailMixin, UsernameMixin):
    pass

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length = 50
    )
    password = forms.CharField(
        widget = forms.PasswordInput()
    )


