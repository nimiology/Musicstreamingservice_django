from django.urls import path
from Users.views import SignUp,LogIn,ForgetPassword,LOGOUT

app_name='Users'
urlpatterns = [
    path('signup',SignUp),
    path('signin',LogIn),
    path('forgetpassword/<SLUG>',ForgetPassword),
    path('logout',LOGOUT)
]