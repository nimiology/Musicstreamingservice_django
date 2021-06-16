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
    Cover = models.ImageField(upload_to=upload_image_path)
    Song = models.FileField(validators=[Validator],upload_to=upload_song_path)


    def __str__(self):
        return self.Title

#TODO: album works but i don't like it this way I have to change manytomany to another relationship in django

