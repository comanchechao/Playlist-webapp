from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a name for your playlist")
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    creater = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Tracks(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a music genre (e.g. Psychedelic Rock)')

    def __str__(self):
        return self.name
