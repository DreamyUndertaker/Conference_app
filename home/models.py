from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    ROLES = (
        ('Admin', 'Admin'),
        ('Speaker', 'Speaker'),
        ('Listener', 'Listener'),
    )
    role = models.CharField(max_length=10, choices=ROLES)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')


class Room(models.Model):
    name = models.CharField(max_length=100)


class Talk(models.Model):
    title = models.CharField(max_length=200)
    speakers = models.ManyToManyField(CustomUser, related_name='talks')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Schedule(models.Model):
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
