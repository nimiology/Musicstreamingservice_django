from django.urls import path
from .views import Search,ALBUM

app_name = 'Songs'
urlpatterns = [
    path('search', Search, name='search'),
    path('Album/<Slug>', ALBUM, name='Album')
]