from songs.models import Album
from songs.permissions import IsArtist
from songs.serializers import AlbumSerializer
from songs.ulitis import CreateRetrieveUpdateDestroyAPIView


class AlbumAPI(CreateRetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'slug'

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
