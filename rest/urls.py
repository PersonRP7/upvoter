from . import views
from django.urls import path

app_name = 'rest'
urlpatterns = [
    path('', views.rest_home, name = 'rest_home'),
    path('username/<str:username>/', views.username, name = 'username'),
    path('picture/', views.PictureView.as_view(), name = 'picture'),
    path('autocomplete/', views.autocomplete, name = 'autocomplete'),
]
