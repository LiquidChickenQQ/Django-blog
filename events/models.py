from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=500)
    maps = models.URLField(null=False)
    date_posted = models.DateTimeField(auto_now=True)


class Pictures(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pics = models.ImageField(upload_to='past_pics')
    details = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now=True)
