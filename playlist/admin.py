from django.contrib import admin
from .models import Playlist, Genre, Song, Artist, Album

admin.site.register(Playlist)
admin.site.register(Genre)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_genre', 'date_of_birth', 'date_of_death')
    fields = ['description', 'name','genre',('date_of_birth', 'date_of_death')]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'display_genre')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'display_genre')
