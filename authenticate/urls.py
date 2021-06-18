from django.urls import path
from .views import SignUp,LogIn

app_name='authenticate'
urlpatterns = [
    path('signup',SignUp),
    path('login',LogIn)
]