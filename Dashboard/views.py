from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from Songs.models import Album, SingleTrack, Playlist
from Users.models import USERSINFO
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
            SongFile = forms.FileField(validators=[Validator])

        if request.method == 'POST':
            UPLOADERFORMS = UPLOADERFORMS(request.POST, request.FILES)
            if UPLOADERFORMS.is_valid():
                DATA = UPLOADERFORMS.cleaned_data
                Track = SingleTrack(Title=DATA['Title'], Album=DATA['Album'],
                                    SongFile=DATA['SongFile'])
                Track.save()
                FEATURES = USERSINFO.objects.filter(USERNAME__in=DATA['Features'])
                Track.Features.set(FEATURES)
                context['SEND'] = 'Succesful!'

        context['FORMS'] = UPLOADERFORMS
        return render(request, 'Dashboard/Trackuploader.html', context)

    return redirect(reverse('Users:SignIn'))


def AlbumAdder(request):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        print(f'[USERNAME] {request.user.username}')
        context = {}

        class ALBUMCREATOR(forms.Form):
            Title = forms.CharField(widget=forms.TextInput())
            Cover = forms.ImageField()

        if request.method == 'POST':
            ALBUMCREATOR = ALBUMCREATOR(request.POST, request.FILES)
            if ALBUMCREATOR.is_valid():
                DATA = ALBUMCREATOR.cleaned_data
                print(DATA)
                MODELALBUM = Album(Title=DATA['Title'],
                                   Artist=USERSINFO.objects.filter(USERNAME__exact=request.user.username)[0],
                                   Cover=DATA['Cover'])
                MODELALBUM.save()
                context['SEND'] = 'Succesful!'

        context['FORMS'] = ALBUMCREATOR
        return render(request, 'Dashboard/AlbumAdder.html', context)
    else:
        return redirect(reverse('Users:SignIn'))


def PlaylistAdder(request):
    if request.user.is_authenticated:
        context = {}

        class FORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput())
            Cover = forms.ImageField(required=False)

        if request.method == 'POST':
            FORMS = FORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                PLAYLIST = Playlist(Title=DATA['Title'],
                                    Owner=USERSINFO.objects.get(USERNAME=request.user.username))
                if DATA['Cover'] != None:
                    PLAYLIST.Cover = DATA['Cover']
                PLAYLIST.save()
                context['SEND'] = 'Created!'
        context['FORMS'] = FORMS
        return render(request, 'Dashboard/PlaylistAdder.html', context)

    return redirect(reverse('Users:SignIn'))


def UserInfo(request):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        print(f'[USERNAME] {request.user.username}')
        user = USERSINFO.objects.get(USERNAME=request.user.username)
        context = {}

        class FormUser(forms.Form):
            NAME = forms.CharField(widget=forms.TextInput(attrs={'value': user.NAME}), required=False)
            USERNAME = forms.CharField(widget=forms.TextInput(attrs={'value': user.USERNAME}), required=False)
            PASSWORD = forms.CharField(widget=forms.PasswordInput(attrs={'value': user.PASSWORD}), required=False)
            PROFILEPIC = forms.ImageField(required=False)

        if request.method == "POST":
            DATA = FormUser(request.POST, request.FILES)
            context['FORMS'] = DATA
            if DATA.is_valid():
                DATA = DATA.cleaned_data
                print(DATA)
                user.NAME = DATA['NAME']
                user.USERNAME = DATA['USERNAME']
                user.PASSWORD = DATA['PASSWORD']
                if DATA['PROFILEPIC'] != None:
                    user.PROFILEPIC = DATA['PROFILEPIC']

                user.save()
                context['SEND'] = 'Data Changed'

        else:
            context['FORMS'] = FormUser

        return render(request, 'Dashboard/UserInfo.html', context)
    else:
        return redirect(reverse('Users:SignIn'))


def EditSong(request, Slug):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        TRACK = SingleTrack.objects.get(Slug=Slug, Album__Artist__USERNAME=request.user.username)
        context = {
            'Track': TRACK
        }

        class FORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput(attrs={'value': TRACK.Title}))
            Album = forms.ModelChoiceField(queryset=Album.objects.filter(Artist__USERNAME__exact=request.user.username),
                                           initial=TRACK.Album)

            CHOICES = []
            for ARTIST in USERSINFO.objects.all():
                if ARTIST.USERNAME != request.user.username:
                    CHOICES.append((ARTIST, ARTIST))

            INITIAL = []
            for artist in TRACK.Features.all():
                INITIAL.append(str(artist))

            Features = forms.MultipleChoiceField(choices=CHOICES, initial=INITIAL, required=False)
            SongFile = forms.FileField(validators=[Validator], required=False)

        if request.method == 'POST':
            FORMS = FORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                print(DATA)
                TRACK.Title = DATA['Title']
                TRACK.Album = DATA['Album']
                if DATA['SongFile'] != None:
                    TRACK.SongFile = DATA['SongFile']
                TRACK.save()
                FETURES = USERSINFO.objects.filter(USERNAME__in=DATA['Features'])
                TRACK.Features.set(FETURES)

        context['FORMS'] = FORMS

        return render(request, 'Dashboard/Trackuploader.html', context)

    return redirect(reverse('Users:SignIn'))


def EditAlbum(request, Slug):
    LOGINSTATUS = request.user.is_authenticated
    if LOGINSTATUS:
        ALBUMS = Album.objects.get(Slug=Slug, Artist__USERNAME=request.user.username)
        context = {
            'Album': ALBUMS
        }

        class FORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput(attrs={'value': ALBUMS.Title}))
            Cover = forms.ImageField(required=False)

        if request.method == 'POST':
            FORMS = FORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                ALBUMS.Title = DATA['Title']
                if DATA['Cover'] != None:
                    ALBUMS.Cover = DATA['Cover']

                ALBUMS.save()
                context['SEND'] = 'Succesful!'
        context['FORMS'] = FORMS

        return render(request, 'Dashboard/AlbumInfo.html', context)
    return redirect(reverse('Users:SignIn'))


def EditPlaylist(request, Slug):
    if request.user.is_authenticated:
        PLAYLIST = Playlist.objects.get(Slug=Slug,Owner__USERNAME=request.user.username)
        context = {}

        class FORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput(attrs={'value':PLAYLIST.Title}))
            Cover = forms.ImageField(required=False)

        if request.method == 'POST':
            FORMS = FORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                if DATA['Cover'] != None:
                    PLAYLIST.Cover = DATA['Cover']

                PLAYLIST.Title = DATA['Title']
                PLAYLIST.save()
                context['SEND'] = 'Created!'
        context['FORMS'] = FORMS
        return render(request, 'Dashboard/PlaylistAdder.html', context)
    return redirect(reverse('Users:SignIn'))

def ALBUMS(request):
    if request.user.is_authenticated:
        LISTALBUMS = Album.objects.filter(Artist__USERNAME__exact=request.user.username)
        context = {
            'ALBUMS': LISTALBUMS
        }
        return render(request, 'Dashboard/ALBUMS.html', context)
    return redirect(reverse('Users:SignIn'))


def Songs(request):
    if request.user.is_authenticated:
        LISTSONGS = SingleTrack.objects.filter(Album__Artist__USERNAME__exact=request.user.username)
        context = {
            'SONGS': LISTSONGS
        }
        return render(request, 'Dashboard/Songs.html', context)
    return redirect(reverse('Users:SignIn'))


def AddSongToPlaylist(request, Slug):
    if request.user.is_authenticated:
        context = {}
        TRACK = SingleTrack.objects.get(Slug=Slug)

        class FORMS(forms.Form):
            USER_PLAYLIST = Playlist.objects.filter(Owner__USERNAME__exact=request.user.username)
            CHOICES = []
            for PLAYLIST in USER_PLAYLIST:
                CHOICES.append((PLAYLIST.Slug, PLAYLIST))

            CHOOSED = []
            for PLAYLIST in TRACK.AddedToPlaylist.filter(Owner__USERNAME__exact=request.user.username):
                CHOOSED.append(str(PLAYLIST.Slug))

            PLAYLISTS = forms.MultipleChoiceField(choices=CHOICES, initial=CHOOSED)

        FORMS = FORMS(request.POST or None)
        if FORMS.is_valid():
            DATA = FORMS.cleaned_data
            print(DATA)
            PLAYLISTS = Playlist.objects.filter(Slug__in=DATA['PLAYLISTS'])
            TRACK.AddedToPlaylist.set(PLAYLISTS)

        context['FORMS'] = FORMS
        return render(request, 'Dashboard/Trackuploader.html', context)
    return redirect(reverse('Users:SignIn'))
