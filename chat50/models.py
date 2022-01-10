from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import related, AutoField
from datetime import datetime

class User(AbstractUser):
    pass

class Room(models.Model):
    name = models.CharField(max_length=256)


class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=64)
    room = models.CharField(max_length=256)    