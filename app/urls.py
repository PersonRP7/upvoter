from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.home, name = 'home'),
    path('create_picture', views.create_picture, name = 'create_picture'),
    path('see_picture/<int:id>/', views.see_picture, name = 'see_picture'),
    path('upvote/<int:id>/', views.upvote, name = 'upvote'),
    path('downvote/<int:id>/', views.downvote, name = 'downvote'),
    path('live', views.live, name = 'live'),
    path('get_votes_count/<int:id>/', views.get_votes_count, name = 'get_votes_count'),
]