from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']
        field_classes = {'username': UsernameField}


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput)
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
