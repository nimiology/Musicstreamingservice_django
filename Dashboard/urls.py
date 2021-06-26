from django.urls import path
from .views import TrackUploader,AlbumAdder,UserInfo,ChangeSongDetail,ChangeAlbumDetail


urlpatterns = [
    path('trackuploader', TrackUploader),
    path('albumadder',AlbumAdder),
    path('userinfo',UserInfo),
    path('Albums/<Slug>', ChangeAlbumDetail),
    path('Song/<Slug>', ChangeSongDetail)
]