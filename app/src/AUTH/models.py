from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Account(User):
    ACCOUNT_MODE = [
        (0, 'User'),
        (1, 'Moderator'),
        (2, 'Admin'),
    ]
    LANGUAGE_CHOICE = [
        ('RU', 'Russian'),
        ('EN', 'English'),
    ]

    mode = models.IntegerField(choices=ACCOUNT_MODE)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICE)
    created_date = models.DateTimeField(default=timezone.now)
    banned = models.BooleanField(default=False)


class AuthHistory(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    success = models.BooleanField(default=True)
