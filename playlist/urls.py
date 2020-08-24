from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'playlist'
urlpatterns = [
    url(r'^$', views.playlist_list, name="list"),
]
