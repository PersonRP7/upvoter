from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path('users_view/', views.users_view, name = 'users'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    # path('login/', views.my_login, name = 'login'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "users/logout.html"), name = 'logout'),
]