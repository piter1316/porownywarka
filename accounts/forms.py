from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Nazwa użytkownika'},
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Hasło'},
    ))
    class Meta:
        fields = ['Username', 'Password']
