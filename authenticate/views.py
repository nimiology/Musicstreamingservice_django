from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from .forms import SIGNUP, LOGIN,FORGET
from .models import USERSINFO


def CREATEUSER(INFO):
    USER = USERSINFO(NAME=INFO['Name'],USERNAME=INFO['UserName'],EMAIL=INFO['Email'],PASSWORD=INFO['Password'],Slug=INFO['UserName'],CREATE=True)
    USER.save()

def SignUp(request):
    LOGINSTATUS = request.user.is_authenticated
    print(f'[LOGIN STATUS]{LOGINSTATUS}')

    if not LOGINSTATUS:
        FORMS = SIGNUP(request.POST or None)

        context = {
            'forms': FORMS
        }

        if FORMS.is_valid():
            DATA = FORMS.cleaned_data
            print(DATA)
            CREATEUSER(DATA)
            context['SIGNUP'] = 'USER CREATED'
            return redirect('/signin')
    else:
        return redirect('/Dashboard')

    return render(request, 'auth/SignUp.html', context)



def LogIn(request):
    LOGINSTATUS = request.user.is_authenticated
    print(f'[LOGIN STATUS]{LOGINSTATUS}')
    if not LOGINSTATUS:
        FORMS = LOGIN(request.POST or None)
        context = {
            'FORMS': FORMS,
            "LOGIN": 'YOU ARE NOT IN!'
        }
        if FORMS.is_valid():
            DATA = FORMS.cleaned_data
            print(DATA)
            username = USERSINFO.objects.filter(EMAIL__exact=DATA['EMAIL'])
            if username.exists():
                username = username.values()[0]['USERNAME']
                USER = authenticate(request, username=username, password=DATA['Password'])
                if USER is not None:
                    login(request, USER)
                    context['LOGIN'] = 'YOU ARE IN!'
                    return redirect('/Dashboard')
            else:
                print("[LOGIN] User doesn't FOUND!")
    else:
        return redirect('/Dashboard')

    return render(request, 'auth/LOGIN.html', context)

def ForgetPassword(request,SLUG):
    QS = USERSINFO.objects.filter(PasswordForget__exact=SLUG)
    context = {}
    if QS.exists():
        QS = QS[0]
        FORMS = FORGET(request.POST or None)
        if FORMS.is_valid():
            DATA = FORMS.cleaned_data
            QS.PASSWORD = DATA['PASSWORD1']
            QS.save()

            context['SEND'] = 'PASSWORD CHANGED!'
        context['FORMS'] = FORMS
        return render(request, 'auth/forgetpassword.html',context)
    raise Http404('Not Found !')