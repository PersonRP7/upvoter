from rest_framework import serializers
from app.models import Picture, User

class UsernameSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']

class PictureIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ['id']

class PictureTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ['title']

class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = "__all__"

# class PictureSerializer(serializers.ModelSerializer):

#     user = serializers.RelatedField(
#         source = 'user',
#         read_only = True
#     )

#     class Meta:
#         model = Picture
#         fields = 
