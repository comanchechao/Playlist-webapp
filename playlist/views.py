from django.shortcuts import render
from playlist.models import Product
from django.views import generic

def playlist_list(request):
    products = Product.objects.all().order_by('created_at');
    context = {
    'products': products,
    }
    return render(request, 'playlist/playlist_list.html', context=context)


# class Playlist_List(generic.ListView):
#     model = Playlist
