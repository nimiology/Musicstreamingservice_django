from django.urls import path
from Users.views import SignUp, LogIn, ForgetPassword, LOGOUT, UserSongs, UserAlbums

app_name='Users'
urlpatterns = [
    path('signup',SignUp),
    path('signin',LogIn),
    path('forgetpassword/<SLUG>',ForgetPassword),
    path('logout',LOGOUT),
    path('<USERNAME>/Songs',UserSongs),
    path('<USERNAME>/Albums',UserAlbums),
]