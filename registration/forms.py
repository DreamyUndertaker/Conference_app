from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.forms import CharField, ChoiceField
from django.utils.translation import gettext_lazy as _
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    ROLES = (
        ('Admin', 'Admin'),
        ('Speaker', 'Speaker'),
        ('Listener', 'Listener'),
    )
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password1 = CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password2 = CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))
    role = forms.ChoiceField(choices=ROLES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']
        field_classes = {'username': UsernameField}


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(
        attrs= {
            'class': 'form-control'
        }
    ))
