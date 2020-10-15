from django.db import models
from django.contrib.auth.models import User
import math
from time import strftime, gmtime
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from .models import User


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="product name")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnails", blank=False)
    created_at = models.DateTimeField(verbose_name='Created At', default=timezone.now)


















    # artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE, default=None)
# class Playlist(models.Model):
# audio_id = models.TextField()
#     title = models.CharField(max_length=200, help_text="Enter a name for your playlist")
#     slug = models.SlugField()
#     date = models.DateTimeField(auto_now_add=True)
#     thumbnail = models.ImageField(default='default.png', blank=True)
#     creater = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title
#
#
# # class Tracks(models.Model):
# #     title = models.CharField(max_length=200)
# #     date = models.DateTimeField(auto_now_add=True)
# #
# #     def __str__(self):
# #         return self.title
#
# class Genre(models.Model):
#     name = models.CharField(max_length=100, help_text='Enter a music genre (e.g. Psychedelic Rock)')
#
#     def __str__(self):
#         return self.name
#
#
# class Artist(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField()
#     description = models.TextField(default=None)
#     genre = models.ManyToManyField(Genre)
#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('Died', null=True, blank=True)
#
#     def display_genre(self):
#         return ', '.join(genre.name for genre in self.genre.all()[:3])
#
#     display_genre.short_description = 'Genre'
#
#     def __str__(self):
#         return self.name
#
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Artist, self).save(*args, **kwargs)
#
#
# class Album(models.Model):
#     name = models.CharField(max_length=50)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     genre = models.ManyToManyField(Genre)
#
#     def display_genre(self):
#         return ', '.join(genre.name for genre in self.genre.all()[:3])
#
#     display_genre.short_description = 'Genre'
#
#     def __str__(self):
#         return self.name
#

    # genre = models.ManyToManyField(Genre)

    # def display_genre(self):
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])
    #
    # display_genre.short_description = 'Genre'

    # @property
    # def duration(self):
    #     return str(strftime('%H:%M:%S', gmtime(float(self.playtime))))
    #
    # @property
    # def file_size(self):
    #     if self.size == 0:
    #         return "0B"
    #     size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    #     i = int(math.floor(math.log(self.size, 1024)))
    #     p = math.pow(1024, i)
    #     s = round(self.size / p, 2)
    #     return "%s %s" % (s, size_name[i])
    #
    #     def __str__(self):
    #         return self.title
