from django.urls import path

from songs.views import AlbumAPI, AlbumsAPI, PlaylistsAPI, PlaylistAPI, TrackAPI, TracksAPI

urlpatterns = [
    path('album/', AlbumAPI.as_view()),
    path('album/<slug>/', AlbumAPI.as_view()),
    path('albums/', AlbumsAPI.as_view()),

    path('playlist/', PlaylistAPI.as_view()),
    path('playlist/<slug>/', PlaylistAPI.as_view()),
    path('playlists/', PlaylistsAPI.as_view()),

    path('track/', TrackAPI.as_view()),
    path('track/<slug>/', TrackAPI.as_view()),
    path('tracks/', TracksAPI.as_view()),
]