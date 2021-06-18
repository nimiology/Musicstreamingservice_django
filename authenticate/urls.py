from django.urls import path
from authenticate.views import SignUp,LogIn

app_name='authenticate'
urlpatterns = [
    path('signup',SignUp),
    path('signin',LogIn)
]