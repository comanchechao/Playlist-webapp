from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'playlist'
urlpatterns = [
    path('playlists', views.Playlist_List.as_view(), name="list"),
]
