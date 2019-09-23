from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsernameSerializer, PictureIdSerializer, PictureTitleSerializer
from .serializers import PictureSerializer
from app.models import Picture, User

def rest_home(request):
    return HttpResponse("rest")

@api_view(['GET'])
def username(request, username):
    # user = User.objects.get(username = username)
    serializer = UsernameSerializer(user)
    return Response(serializer.data)

class PictureView(generics.ListAPIView):

    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

def autocomplete(request):
    return render(
        request, 'rest/autocomplete.html'
    )



