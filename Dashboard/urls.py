from django.urls import path
from .views import TrackUploader,AlbumAdder
urlpatterns = [
    path('trackuploader', TrackUploader),
    path('albumadder',AlbumAdder)
]