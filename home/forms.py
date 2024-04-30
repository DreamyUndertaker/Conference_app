from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Room, Talk, CustomUser


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ['title', 'speakers', 'room', 'start_time', 'end_time']


class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'role']
