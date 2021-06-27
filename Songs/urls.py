from django.urls import path
from .views import Search,ALBUM,SINGLETRACK

app_name = 'Songs'
urlpatterns = [
    path('search', Search, name='search'),
    path('Album/<Slug>', ALBUM, name='Album'),
    path('singletrack/<Slug>', SINGLETRACK, name='SingleTrack'),
]