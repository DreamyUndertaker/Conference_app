from django.db import models
from django.utils.translation import gettext_lazy as _
from registration.models import CustomUser


class Room(models.Model):
    name = models.CharField(_('Name'), max_length=100)


class Talk(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    speakers = models.ManyToManyField(CustomUser, related_name='talks')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(_('Start Time'))
    end_time = models.DateTimeField(_('End Time'))
    youtube_video_id = models.CharField(max_length=20, blank=True, null=True)


class Schedule(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(_('Start Time'))
    end_time = models.DateTimeField(_('End Time'))


