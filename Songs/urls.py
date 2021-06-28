from django.urls import path
from .views import Search,ALBUM,SINGLETRACK, PLAYLIST

app_name = 'Songs'
urlpatterns = [
    path('search', Search, name='search'),
    path('Albums/<Slug>', ALBUM, name='Album'),
    path('Songs/<Slug>', SINGLETRACK, name='Song'),
    path('Playlists/<Slug>', PLAYLIST, name='Playlist'),
]