from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_captcha(value):
    if value != 'No':
        raise ValidationError(
            ("You are a robot."),
            params = {'value':value}
        )

def validate_password_length(value):
    if len(value) < 10:
        raise ValidationError(
            ("Password has to be longer than 9 characters."),
            params = {'value':value}
        )

def validate_password_number(value):
    isdigit_values = []
    for i in value:
        isdigit_values.append(i.isdigit())
    if True not in isdigit_values:
        raise ValidationError(
            ("Password has to include at least one number."),
            params = {'value':value}
        )

# up_case = f"{pw[0][0].upper()}{pw[0][1:]}"
# def validate_password_password(value):
#     disallowed = ['password', 'Password']
#     for i in disallowed:
#         if value == i:
#             raise ValidationError(
#                 (f"Password cannot contain {value}."),
#                 params = {'value':value}
#             )

def validation_error(value):
    raise ValidationError(
        f"Password cannot contain {value}.",
        params = {'value':value}
    )

def validate_password_password(value):
    if 'Password' in value:
        validation_error(value)
    if 'password' in value:
        validation_error(value)
        
# def validate_password_password(value):
#     if 'password' in value or 'Password' in value:
#         string = ""
#         for i in value:
#             if i.isalpha():
#                 string += i
#         raise ValidationError(f"Password cannot contain {string}.", params = {'value':value})

def validate_username(value):
    if User.objects.filter(username = value).exists():
        raise ValidationError(
            (f"{value} is taken."),
            params = {'value':value}
        )

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError(
            (f"{value} is taken."),
            params = {'value':value}
        )