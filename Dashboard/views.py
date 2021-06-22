from django.shortcuts import render,redirect
from django import forms
from Songs.models import Album,SingleTrack
from authenticate.models import USERSINFO
from Songs.Ulitis import Validator


def TrackUploader(request):
    LOGINSTATUS = request.user.is_authenticated
    print(f'[USERNAME] {request.user.username}')
    if LOGINSTATUS:
        context = {}


        class UPLOADERFORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput())
            Album = forms.ModelChoiceField(queryset=Album.objects.filter(Artist__USERNAME__contains=request.user.username))

            ARTIST = USERSINFO.objects.all()
            CHOICES = []
            for i in range(0,len(ARTIST)):
                CHOICES.append((ARTIST[i],ARTIST[i]))

            Features = forms.MultipleChoiceField(choices=CHOICES,required=False)
            Producer = forms.CharField(widget=forms.TextInput())
            SongFile = forms.FileField(validators=[Validator])

        if request.method == 'POST':
            FORMS =  UPLOADERFORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                DATA = FORMS.cleaned_data
                print(DATA)
                Track = SingleTrack(Title=DATA['Title'],Slug=DATA['Title'],Album=DATA['Album'], Producers=DATA['Producer'],SongFile=DATA['SongFile'])
                Track.save()
                FEATURES = USERSINFO.objects.filter(USERNAME__in=DATA['Features'])
                print(FEATURES)
                Track.Features.set(FEATURES)
                context['SEND'] = 'Succesful!'


        else:
            FORMS = UPLOADERFORMS

        context['FORMS'] = FORMS
        return render(request, 'Dashboard/Trackuploader.html', context)
    else:
        return redirect('/signin')


# class ALBUMCREATOR(forms.Form):
#     Title = forms.CharField(widget=forms.TextInput())
#     #User
#     Album = forms.ModelChoiceField()
#     Cover = forms.ImageField()