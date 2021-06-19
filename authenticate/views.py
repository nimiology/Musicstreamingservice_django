from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from .forms import SIGNUP, LOGIN
from .models import USERSINFO

def CREATEUSER(INFO):
    USER = USERSINFO(USERNAME=INFO['UserName'],EMAIL=INFO['Email'],PASSWORD=INFO['Password'])
    USER.save()

def SignUp(request):
    print(f'[LOGIN STATUS]{request.user.is_authenticated}')
    FORMS = SIGNUP(request.POST or None)

    context = {
        'forms': FORMS
    }

    if FORMS.is_valid():
        USER = get_user_model()
        DATA = FORMS.cleaned_data
        qs = USER.objects.create_user(username=DATA['UserName'], email=DATA['Email'], password=DATA['Password'])
        CREATEUSER(DATA)
        print(DATA)
        context['SIGNUP'] = 'USER CREATED'
        return redirect('/signin')

    return render(request, 'auth/SignUp.html', context)


#TODO: IF HE WAS LOGIN REDIRECT TO ADMIN
#TODO: EVERY USER CAN SEND HIS MUSIC AND ADD IT
#TODO: CHANGE PASSWORD AND USER NAME FEATURE
#TODO: ADD PROFILE PIC WHEN ADMIN PANNEL IS READY

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
        username = USERSINFO.objects.filter(EMAIL=DATA['EMAIL'])
        print(username)
        try:
            username = username.values()[0]['USERNAME']
            USER = authenticate(request, username=username, password=DATA['Password'])
            if USER is not None:
                login(request, USER)
                context['LOGIN'] = 'YOU ARE IN!'
                return redirect('/')
        except:
            print("[LOGIN] User doesn't FOUND!")

    return render(request, 'auth/LOGIN.html', context)
