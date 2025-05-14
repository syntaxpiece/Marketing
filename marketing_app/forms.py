from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'User Name',
        'class':'form-control custom-input m-3'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Email',
        'class':'form-control custom-input m-3'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'form-control custom-input m-3'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class':'form-control custom-input m-3'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'User Name',
        'class':'form-control custom-input m-3'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password',
        'class':'form-control custom-input m-3'
    }))

class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['name', 'description', 'location', 'gender', 'img', 'video', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control custom-input m-3'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'form-control custom-input m-3'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control custom-input m-3'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control custom-input m-3'
            }),
            'birthday': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control custom-input m-3'
            }),
            'img': forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control custom-input m-3'
            }),
            'video': forms.FileInput(attrs={
                'type': 'file',
                'class': 'form-control custom-input m-3'
            }),
        }
