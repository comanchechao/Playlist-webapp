from django.db import models

class Playlist(models.Model):
    title = models.CharField(max_length=200, help_text="Enter a name for your playlist")
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    creater = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
