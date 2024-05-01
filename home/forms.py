from django import forms

from home.models import Room, Talk


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']


class TalkForm(forms.ModelForm):
    class Meta:
        model = Talk
        fields = ['title', 'speakers', 'room', 'start_time', 'end_time']
