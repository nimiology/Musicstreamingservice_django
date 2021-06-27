from django.urls import path
from authenticate.views import SignUp,LogIn,ForgetPassword,LOGOUT

app_name='authenticate'
urlpatterns = [
    path('signup',SignUp),
    path('signin',LogIn),
    path('forgetpassword/<SLUG>',ForgetPassword),
    path('logout',LOGOUT)
]