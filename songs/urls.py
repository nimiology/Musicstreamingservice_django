from django.urls import path

from songs.views import AlbumAPI, AlbumsAPI, PlaylistsAPI, PlaylistAPI

urlpatterns = [
    path('album/', AlbumAPI.as_view()),
    path('album/<slug>/', AlbumAPI.as_view()),
    path('albums/', AlbumsAPI.as_view()),

    path('playlist/', PlaylistAPI.as_view()),
    path('playlist/<slug>/', PlaylistAPI.as_view()),
    path('playlists/', PlaylistsAPI.as_view()),
]