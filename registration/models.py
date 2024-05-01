from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    ROLES = (
        ('Admin', 'Admin'),
        ('Speaker', 'Speaker'),
        ('Listener', 'Listener'),
    )
    role = models.CharField(_('Role'), max_length=10, choices=ROLES)
    user_groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    custom_user_groups = models.ManyToManyField(Group, related_name='custom_users')
