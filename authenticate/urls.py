from django.urls import path
from authenticate.views import SignUp,LogIn,ForgetPassword

app_name='authenticate'
urlpatterns = [
    path('signup',SignUp),
    path('signin',LogIn),
    path('forgetpassword/<SLUG>',ForgetPassword)
]