from django.urls import path
from Users.views import SignUp, SignIn, ForgetPassword, LOGOUT, UserSongs, UserAlbums

app_name = 'Users'
urlpatterns = [
    path('signup', SignUp, name='SignUp'),
    path('signin', SignIn, name='SignIn'),
    path('forgetpassword/<SLUG>', ForgetPassword, name='ForgetPassword'),
    path('logout', LOGOUT, name='logout'),
    path('<USERNAME>/Songs', UserSongs, name='UserSongs'),
    path('<USERNAME>/Albums', UserAlbums, name='UserAlbum'),
]
