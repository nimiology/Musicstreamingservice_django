from django.shortcuts import render,redirect
from .forms import SIGNUP
# Create your views here.
#TODO: SIGN UP
def SignUp(request):
    print(f'[LOGIN STATUS]{request.user.is_authenticated}')
    FORMS = SIGNUP(request.POST or None)
    if not request.user.is_authenticated:
        context = {
            'forms':FORMS
        }
        return render(request, 'auth/SignUp.html', context)
    else:
        context = {
            'forms': FORMS
        }
        return render(request, 'auth/SignUp.html', context)
#TODO: SIGN IN