from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterCaptchaForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
import traceback
from django.conf import settings


def users_view(request):
    return HttpResponse("some response")

@login_required
def profile(request):
    return HttpResponse(request.user.username)

def send_email(user, request, form):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    message = render_to_string('users/activate_account.html', {
        'user':user,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token':account_activation_token.make_token(user),
    })
    to_email = form.cleaned_data.get('email')
    email = EmailMessage(email_subject, message, to = [to_email])
    email.send()


def register_get(request, messages, redirect, UserRegisterCaptchaForm):
    if User.objects.filter(
        username = request.user.username
    ).exists():
        messages.info(request, "You already have an account.")
        return redirect('users:profile')
    form = UserRegisterCaptchaForm()
    return render(request, 'users/register.html', {'form':form})


def register_post(request, messages, redirect, UserRegisterCaptchaForm):
    try:
        form = UserRegisterCaptchaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            user.is_active = False
            user.save()
            if user:
                send_email(user, request, form)
                return HttpResponse("Email sent.")
        else:
            messages.info(request, "Form not correct.")
            return render(
                request,
                'users/register.html',
                {'form':form}
            )
    except Exception as e:
        logging.error(traceback.format_exc())


def register(request):
    if request.method == 'GET':
        return register_get(request, messages, redirect, UserRegisterCaptchaForm)
    elif request.method == 'POST':
        return register_post(request, messages, redirect, UserRegisterCaptchaForm)


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Account activated.')
    else:
        return HttpResponse('Link incorrect.')


