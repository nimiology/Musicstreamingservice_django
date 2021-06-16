from django import forms

class SEARCH(forms.Form):
    Search = forms.CharField(widget=forms.TextInput())