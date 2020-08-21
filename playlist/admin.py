from django.contrib import admin
from .models import Playlist, Genre, Tracks

admin.site.register(Playlist)
admin.site.register(Genre)
admin.site.register(Tracks)
