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
            # bug
            Features = forms.MultipleChoiceField(choices='')
            Producer = forms.CharField(widget=forms.TextInput())
            SongFile = forms.FileField()

        FORMS =  UPLOADERFORMS(request.POST or None)
        context = {
            'FORMS' : FORMS
        }
        return render(request, 'Dashboard/Trackuploader.html', context)



# class ALBUMCREATOR(forms.Form):
#     Title = forms.CharField(widget=forms.TextInput())
#     #User
#     Album = forms.ModelChoiceField()
#     Cover = forms.ImageField()