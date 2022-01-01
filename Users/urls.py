from django.template.defaulttags import url
from django.urls import path, include

app_name = 'Users'
urlpatterns = [
    url('auth/', include('djoser.urls')),
    url('auth/', include('djoser.urls.jwt'))
]
