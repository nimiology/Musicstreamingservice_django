from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from .forms import SIGNUP, LOGIN
from .models import USERSINFO
from django import forms
from Songs.Ulitis import slug_genrator
from django.contrib.auth.models import User

def CREATEUSER(INFO):
    USER = USERSINFO(NAME=INFO['Name'],USERNAME=INFO['UserName'],EMAIL=INFO['Email'],PASSWORD=INFO['Password'],Slug=INFO['UserName'])
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
            USER = get_user_model()
            DATA = FORMS.cleaned_data
            print(DATA)
            CREATEUSER(DATA)
            context['SIGNUP'] = 'USER CREATED'
            return redirect('/signin')
    else:
        return redirect('/Dashboard')

    return render(request, 'auth/SignUp.html', context)

#TODO: EVERY USER CAN SEND HIS MUSIC AND ADD IT
#TODO: CHANGE PASSWORD AND USER NAME FEATURE
#TODO: ADD PROFILE PIC WHEN ADMIN PANNEL IS READY

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
            username = USERSINFO.objects.filter(EMAIL=DATA['EMAIL'])
            print(username)
            try:
                username = username.values()[0]['USERNAME']
                USER = authenticate(request, username=username, password=DATA['Password'])
                if USER is not None:
                    login(request, USER)
                    context['LOGIN'] = 'YOU ARE IN!'
                    return redirect('/Dashboard')
            except:
                print("[LOGIN] User doesn't FOUND!")
    else:
        return redirect('/Dashboard')

    return render(request, 'auth/LOGIN.html', context)

def ForgetPassword(request,SLUG):
    QS = USERSINFO.objects.filter(PasswordForget__exact=SLUG)
    context = {}
    if QS.exists():
        QS = QS[0]
        print(QS)

        class FORGET(forms.Form):
            PASSWORD1 = forms.CharField(widget=forms.PasswordInput)
            PASSWORD2 = forms.CharField(widget=forms.PasswordInput)
            def clean(self):
                DATA = self.cleaned_data
                if DATA['PASSWORD1'] != DATA['PASSWORD2']:
                    raise forms.ValidationError("PASSWORD doesn't match1")
                return DATA

        FORMS = FORGET(request.POST or None)
        if FORMS.is_valid():
            DATA = FORMS.cleaned_data
            QS.PASSWORD = DATA['PASSWORD1']

            QS.save()
            #todo: USER DOESN'T WORKS
            u = User.objects.get(username=QS.USERNAME)
            u.password = DATA['PASSWORD1']
            u.save()
            context['SEND'] = 'PASSWORD CHANGED!'
            print(User.objects.get(username=QS.USERNAME).password)
        context['FORMS'] = FORMS
        return render(request, 'auth/forgetpassword.html',context)