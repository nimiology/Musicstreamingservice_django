from django.db import models
from .Ulitis import Validator,upload_image_path,upload_song_path

class Album(models.Model):
    Title = models.CharField(max_length=1000)
    Artist = models.CharField(max_length=1000)
    Cover = models.ImageField(upload_to=upload_image_path,unique=True)
    Slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Title


class SingleTrack(models.Model):
    Title = models.CharField(max_length=1000)
    Artist = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    Album = models.ManyToManyField(Album, related_name="Album")
    Features = models.CharField(max_length=2048,blank=True)
    Producers = models.CharField(max_length=1000)
    TrackNumber = models.IntegerField(default=0)
    DiscNumber = models.IntegerField(default=0)
    SongFile = models.FileField(validators=[Validator],upload_to=upload_song_path,unique=True)

    def __str__(self):
        return self.Title

#TODO: album works but i don't like it this way I have to change manytomany to another relationship in django

