from django.urls import path
from .views import TrackUploader,PlaylistAdder, AlbumAdder, UserInfo, EditSong, EditAlbum, ALBUMS, Songs

app_name = 'Dashboard'
urlpatterns = [
    path('Songs/Add', TrackUploader, name='TrackUploader'),
    path('Albums/Add', AlbumAdder, name='AlbumAdder'),
    path('userinfo', UserInfo, name='userinfo'),
    path('Albums/<Slug>', EditAlbum, name='EditAlbum'),
    path('Songs/<Slug>', EditSong, name='EditSong'),
    path('Albums', ALBUMS, name='Albums'),
    path('Songs', Songs, name='Songs'),
    path('Playlists/Add',PlaylistAdder, name='PlaylistAdder')
]
