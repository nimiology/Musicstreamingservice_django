from django.urls import path
from .views import Search

app_name = 'Songs'
urlpatterns = [
    path('search',Search)
]