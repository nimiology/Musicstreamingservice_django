from django.urls import path
from .views import TrackUploader,AlbumAdder,UserInfo


urlpatterns = [
    path('trackuploader', TrackUploader),
    path('albumadder',AlbumAdder),
    path('userinfo',UserInfo),
]