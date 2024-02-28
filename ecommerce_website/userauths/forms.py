from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "placeholder":"Username"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "type":"email",
        "placeholder":"Email"
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password",
        "placeholder":"Password"
    }))

    password2 = None

    class Meta:
        model = User
        fields = ['username','email']