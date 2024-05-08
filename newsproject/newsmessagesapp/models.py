from django.db import models
from django.contrib.auth.models import User
from newsapp.models import Post
from datetime import datetime


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=39)
    message = models.TextField()
    pub_date = models.DateTimeField(default=datetime.utcnow)


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Response(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()





