from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=UserProfile.USER_TYPE, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
