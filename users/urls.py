from django.urls import path, include, re_path


urlpatterns = [
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.jwt'))
]
