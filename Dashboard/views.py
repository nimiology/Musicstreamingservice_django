from django.shortcuts import render
from django import forms
from Songs.models import Album,SingleTrack
from authenticate.models import USERSINFO


def TrackUploader(request):
    LOGINSTATUS = request.user.is_authenticated
    print(f'[USERNAME] {request.user.username}')
    if LOGINSTATUS:
        class UPLOADERFORMS(forms.Form):
            Title = forms.CharField(widget=forms.TextInput())
            Album = forms.ModelChoiceField(queryset=Album.objects.filter(Artist__USERNAME__contains=request.user.username))
            ARTIST = USERSINFO.objects.all()
            Features = forms.MultipleChoiceField(choices=((1,'a'),(2,'b')))
            Producer = forms.CharField(widget=forms.TextInput())
            SongFile = forms.FileField()
        if request.method == 'POST':
            FORMS =  UPLOADERFORMS(request.POST, request.FILES)
            if FORMS.is_valid():
                print(FORMS.cleaned_data)
        else:
            FORMS = UPLOADERFORMS

        context = {
            'FORMS' : FORMS
        }
        return render(request, 'Dashboard/Trackuploader.html', context)



# class ALBUMCREATOR(forms.Form):
#     Title = forms.CharField(widget=forms.TextInput())
#     #User
#     Album = forms.ModelChoiceField()
#     Cover = forms.ImageField()