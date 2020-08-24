from django.shortcuts import render
from playlist.models import Playlist, Genre, Artist, Album, Song

def playlist_list(request):
    playlists = Playlist.objects.all().order_by('date');
    context = {
    'playlists': playlists,
    }
    return render(request, 'playlist/index.html', context=context)
