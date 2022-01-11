from rest_framework import serializers
from djoser.serializers import UserSerializer

from songs.models import Album, Playlist


class AlbumSerializer(serializers.ModelSerializer):
    artist = UserSerializer(required=False)

    class Meta:
        model = Album
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True},
            'createdTime': {'read_only': True},
        }


class PlaylistSerializer(serializers.ModelSerializer):
    artist = UserSerializer(required=False)

    class Meta:
        model = Playlist
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True},
            'createdTime': {'read_only': True},
            'lastEdit': {'read_only': True},
        }
