from django.urls import path

from songs.views import AlbumAPI, UserAlbumAPI

urlpatterns = [
    path('album/', AlbumAPI.as_view()),
    path('album/<slug>/', AlbumAPI.as_view()),
    path('albums/', UserAlbumAPI.as_view()),

]