from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control right-angle',
            'value': 'postman',
        }))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control right-angle',
            'placeholder': 'Пароль для входу'
        }))


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control right-angle',
            'value': 'eugene',
        }))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control right-angle',
            'placeholder': 'Пароль для входу'
        }))
