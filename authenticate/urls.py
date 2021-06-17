from django.urls import path
from .views import SignUp

app_name='authenticate'
urlpatterns = [
    path('signup',SignUp)
]