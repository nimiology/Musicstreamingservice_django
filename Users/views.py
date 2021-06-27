from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import SIGNUP, LOGIN, FORGET
from .models import USERSINFO
from Songs.models import SingleTrack, Album


def CREATEUSER(INFO):
    USER = USERSINFO(NAME=INFO['Name'], USERNAME=INFO['UserName'], EMAIL=INFO['Email'], PASSWORD=INFO['Password'],
                     Slug=INFO['UserName'], CHANGE=False)
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
            return redirect(reverse('Users:SignIn'))
    else:
        #todo : MAKE THIS DYNAMIC
        return redirect('/Dashboard')

    return render(request, 'Users/SignUp.html', context)


def SignIn(request):
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
        # todo : MAKE THIS DYNAMIC
        return redirect('/Dashboard')

    return render(request, 'Users/LOGIN.html', context)


def ForgetPassword(request, SLUG):
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
            return redirect(reverse('Users:SignIn'))
        context['FORMS'] = FORMS
        return render(request, 'Users/forgetpassword.html', context)
    raise Http404('Not Found !')


def LOGOUT(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect(reverse('Users:SignIn'))


def UserSongs(request, USERNAME):
    SONG_LIST = SingleTrack.objects.filter(Album__Artist__Slug__exact=USERNAME)
    print(SONG_LIST)
    context = {
        'SONGS': SONG_LIST
    }
    return render(request, 'Users/Songs.html', context)


def UserAlbums(request, USERNAME):
    ALBUMS_LIST = Album.objects.filter(Artist__Slug__exact=USERNAME)
    print(ALBUMS_LIST)
    context = {
        'ALBUMS': ALBUMS_LIST
    }
    return render(request, 'Users/Albums.html', context)
