from rest_framework import serializers
from djoser.serializers import UserSerializer

from songs.models import Album, Playlist, Track


class AlbumSerializer(serializers.ModelSerializer):
    artist = UserSerializer(required=False)

    class Meta:
        model = Album
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True},
            'createdTime': {'read_only': True},
        }


class TrackSerializer(serializers.ModelSerializer):
    artist = UserSerializer(required=False)

    class Meta:
        model = Track
        fields = '__all__'
        extra_kwargs = {
            'slug': {'read_only': True},
            'createdTime': {'read_only': True},
        }

    def to_representation(self, instance):
        self.fields['album'] = AlbumSerializer()
        self.fields['features'] = UserSerializer(many=True)
        return super(TrackSerializer, self).to_representation(instance)


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

    def to_representation(self, instance):
        self.fields['tracks'] = TrackSerializer(many=True)
        return super(PlaylistSerializer, self).to_representation(instance)
