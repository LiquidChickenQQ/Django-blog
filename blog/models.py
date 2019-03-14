from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Post(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField(default='Enter a URL')
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


