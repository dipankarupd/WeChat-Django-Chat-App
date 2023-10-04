from django.db import models
from datetime import datetime
# Create your models here.

class Room(models.Model):
    room = models.CharField(max_length=10000)


class Message(models.Model):
    username = models.CharField(max_length=10000)
    messaege = models.CharField(max_length=1000000)
    time = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=100000)