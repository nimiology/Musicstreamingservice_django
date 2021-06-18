from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import SIGNUP
# Create your views here.
#TODO: SIGN UP
def SignUp(request):
    print(f'[LOGIN STATUS]{request.user.is_authenticated}')
    FORMS = SIGNUP(request.POST or None)

    if FORMS.is_valid():
        USER = get_user_model()
        DATA = FORMS.cleaned_data
        qs = USER.objects.create_user(username=DATA['UserName'],email=DATA['Email'],password=DATA['Password1'])
        print(qs)

    context = {
        'forms':FORMS
    }
    return render(request, 'auth/SignUp.html', context)
    #TODO: IF HE WAS LOGIN REDIRECT TO ADMIN

#TODO: SIGN IN