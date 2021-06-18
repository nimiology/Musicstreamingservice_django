from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from .forms import SIGNUP, LOGIN


def SignUp(request):
    print(f'[LOGIN STATUS]{request.user.is_authenticated}')
    FORMS = SIGNUP(request.POST or None)

    context = {
        'forms': FORMS
    }

    if FORMS.is_valid():
        USER = get_user_model()
        DATA = FORMS.cleaned_data
        qs = USER.objects.create_user(username=DATA['UserName'], email=DATA['Email'], password=DATA['Password1'])
        print(DATA)
        context['SIGNUP'] = 'USER CREATED'
        return redirect('/signin')

    return render(request, 'auth/SignUp.html', context)


#TODO: IF HE WAS LOGIN REDIRECT TO ADMIN
#TODO: ADD EMIAL FOR AUTHENTICATE

def LogIn(request):
    print(f'[LOGIN STATUS]{request.user.is_authenticated}')
    FORMS = LOGIN(request.POST or None)

    context = {
        'FORMS': FORMS,
        "LOGIN": 'YOU ARE NOT IN!'
    }

    if FORMS.is_valid():
        DATA = FORMS.cleaned_data
        print(DATA)
        USER = authenticate(request, username=DATA['UserName'], password=DATA['Password'])
        if USER is not None:
            print('[USER] FOUND!')
            login(request, USER)
            context['LOGIN'] = 'YOU ARE IN!'
            return redirect('/')
        else:
            print('[USER] NOT FOUND!')

    return render(request, 'auth/LOGIN.html', context)
