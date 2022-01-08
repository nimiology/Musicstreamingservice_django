from rest_framework import serializers
from djoser.serializers import UserSerializer

from songs.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    artist = UserSerializer(required=False)

    class Meta:
        model = Album
        fields = '__all__'
