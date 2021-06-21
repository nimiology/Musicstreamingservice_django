from django.urls import path
from .views import TrackUploader
urlpatterns = [
    path('trackuploader', TrackUploader)
]