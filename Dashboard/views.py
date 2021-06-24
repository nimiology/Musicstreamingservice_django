from django.shortcuts import render, redirect
from django import forms
from Songs.models import Album, SingleTrack
from authenticate.models import USERSINFO
from Songs.Ulitis import Validator


def TrackUploader(request):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        print(f'[USERNAME] {request.user.username}')
        context = {}

        class UPLOADERFORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput())
            Album = forms.ModelChoiceField(
                queryset=Album.objects.filter(Artist__USERNAME__contains=request.user.username))

            ARTIST = USERSINFO.objects.all()
            CHOICES = []
            for i in range(0, len(ARTIST)):
                if ARTIST[i].USERNAME != request.user.username:
                    CHOICES.append((ARTIST[i], ARTIST[i]))

            Features = forms.MultipleChoiceField(choices=CHOICES, required=False)
            Producer = forms.CharField(widget=forms.TextInput())
            SongFile = forms.FileField(validators=[Validator])

        if request.method == 'POST':
            FORMS = UPLOADERFORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                print(DATA)
                Track = SingleTrack(Title=DATA['Title'], Album=DATA['Album'], Producers=DATA['Producer'],
                                    SongFile=DATA['SongFile'])
                Track.save()
                FEATURES = USERSINFO.objects.filter(USERNAME__in=DATA['Features'])
                Track.Features.set(FEATURES)
                context['SEND'] = 'Succesful!'
        else:
            FORMS = UPLOADERFORMS

        context['FORMS'] = FORMS
        return render(request, 'Dashboard/Trackuploader.html', context)
    else:
        return redirect('/signin')


def AlbumAdder(request):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        print(f'[USERNAME] {request.user.username}')
        context = {}
        class ALBUMCREATOR(forms.Form):
            Title = forms.CharField(widget=forms.TextInput())
            Cover = forms.ImageField()

        if request.method == 'POST':
            FORMS = ALBUMCREATOR(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                print(DATA)
                MODELALBUM = Album(Title=DATA['Title'],
                                   Artist=USERSINFO.objects.filter(USERNAME__exact=request.user.username)[0],
                                   Cover=DATA['Cover'])
                MODELALBUM.save()
                context['SEND'] = 'Succesful!'
        else:
            FORMS = ALBUMCREATOR
        context['FORMS'] = FORMS
        return render(request,'Dashboard/AlbumAdder.html',context)
    else:
        return redirect('/signin')

def User(request):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        print(f'[USERNAME] {request.user.username}')
        context = {}
        class USER(forms.Form):
            NAME = forms.CharField(widget=forms.TextInput())
            USERNAME = forms.CharField(widget=forms.TextInput())
            PASSWORD = forms.CharField(widget=forms.PasswordInput())
            PROFILEPIC = forms.ImageField()
    else:
        return redirect('/signin')

