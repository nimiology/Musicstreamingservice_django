from django import forms
from Songs.models import Album,SingleTrack
from authenticate.models import USERSINFO

class MUSICGIVER(forms.Form):
    Title = forms.CharField(widget=forms.TextInput())
    #bug
    Album = forms.ModelChoiceField(queryset=Album.objects.filter(Artist=''))
    #bug
    Features = forms.MultipleChoiceField(choices='')
    Producer = forms.CharField(widget=forms.TextInput())
    SongFile = forms.FileField()


class ALBUMCREATOR(forms.Form):
    Title = forms.CharField(widget=forms.TextInput())
    #User
    Album = forms.ModelChoiceField()
    Cover = forms.ImageField()