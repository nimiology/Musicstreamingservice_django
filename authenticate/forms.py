from django import forms
from django.contrib.auth import get_user_model

USER = get_user_model()
class SIGNUP(forms.Form):
    UserName = forms.CharField(
        widget=forms.TextInput())

    Email = forms.CharField(
        widget=forms.EmailInput())

    Password = forms.CharField(
        label='Password',
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
        USERNAME = self.cleaned_data['UserName']
        qs = USER.objects.filter(username=USERNAME)
        if qs.exists():
            raise forms.ValidationError('Usename is already taken')
        return USERNAME
    def clean(self):
        DATA =self.cleaned_data
        pass1 = DATA['Password']
        pass2 = DATA['Password2']
        if len(pass1)<8:
            raise forms.ValidationError("PASSWORD must be 8 letter at least!")
        elif pass1 != pass2:
            raise forms.ValidationError("PASSWORD doesn't match1")
        return DATA

class LOGIN(forms.Form):
    EMAIL = forms.CharField(
        widget=forms.EmailInput())
    Password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean(self):
        DATA = self.cleaned_data
        PASSWORD = DATA['Password']
        if len(PASSWORD)<8:
            raise forms.ValidationError("PASSWORD must be 8 letter at least!")
        return DATA