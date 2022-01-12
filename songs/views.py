from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from songs.models import Album, Playlist, Track
from songs.permissions import IsArtist
from songs.serializers import AlbumSerializer, PlaylistSerializer, TrackSerializer
from songs.ulitis import CreateRetrieveUpdateDestroyAPIView


class AlbumAPI(CreateRetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'slug'

    def post(self, request, *args, **kwargs):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.permission_classes = [IsArtist]
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.permission_classes = [IsArtist]
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(artist=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(artist=self.request.user)


class AlbumsAPI(ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filterset_fields = ['artist', 'title']


class PlaylistAPI(AlbumAPI):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()


class PlaylistsAPI(ListAPIView):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    filterset_fields = ['artist', 'title']


class TrackAPI(AlbumAPI):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class TracksAPI(ListAPIView):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    filterset_fields = ['artist', 'title', 'album', 'features']
