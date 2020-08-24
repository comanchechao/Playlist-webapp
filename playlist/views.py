from django.shortcuts import render
from playlist.models import Playlist, Genre, Artist, Album, Song
from django.views import generic

# def playlist_list(request):
#     playlists = Playlist.objects.all().order_by('date');
#     context = {
#     'playlists': playlists,
#     }
#     return render(request, 'playlist/index.html', context=context)


class Playlist_List(generic.ListView):
    model = Playlist
