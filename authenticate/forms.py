from django import forms
from django.contrib.auth import get_user_model

USER = get_user_model()
#TODO: FIX FUNCTIONS
class SIGNUP(forms.Form):
    UserName = forms.CharField(
        widget=forms.TextInput())

    Email = forms.CharField(
        widget=forms.EmailInput())

    Password1 = forms.CharField(
        widget=forms.PasswordInput())

    Password2 = forms.CharField(
        label='Password confrim',
        widget=forms.PasswordInput(
        ))

    def clean_Email(self):
        EMAIL = self.cleaned_data['Email']
        qs = USER.objects.filter(email=EMAIL)
        if qs.exists():
            raise forms.ValidationError('Email is already taken')
        return EMAIL

    def clean_UserName(self):
        p
    def clean(self):
        DATA =self.cleaned_data
        pass1 = DATA['Password1']
        pass2 = DATA['Password2']
        if pass1 != pass2:
            raise forms.ValidationError("PASSWORD doesn't match")
        return DATA