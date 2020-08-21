from django.contrib import admin
from .models import Playlist, Genre, Song

admin.site.register(Playlist)
admin.site.register(Genre)
admin.site.register(Song)
