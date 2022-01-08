from rest_framework import serializers

from songs.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        exclude = ['slug']

