from django.db import models
from .Ulitis import Validator,upload_image_path,upload_song_path

# Create your models here.
#TODO: use many to many for ARTIST
class SingleTrack(models.Model):
    Title = models.CharField(max_length=1000)
    Artist = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    Cover = models.ImageField(upload_to=upload_image_path)
    Song = models.FileField(validators=[Validator],upload_to=upload_song_path)


    def __str__(self):
        return self.Title