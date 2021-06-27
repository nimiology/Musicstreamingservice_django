from django.urls import path
from .views import TrackUploader, AlbumAdder, UserInfo, ChangeSongDetail, ChangeAlbumDetail, ALBUMS, Songs

urlpatterns = [
    path('trackuploader', TrackUploader),
    path('albumadder',AlbumAdder),
    path('userinfo',UserInfo),
    path('Albums/<Slug>', ChangeAlbumDetail),
    path('Songs/<Slug>', ChangeSongDetail),
    path('Albums',ALBUMS),
    path('Songs',Songs)
]