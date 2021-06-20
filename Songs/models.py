from django.db import models
from django.db.models.signals import pre_save
from .Ulitis import Validator, upload_image_path, upload_song_path, unique_slug_generator
from authenticate.models import USERSINFO


class Album(models.Model):
    Title = models.CharField(max_length=1000)
    Artist = models.ForeignKey(USERSINFO, on_delete=models.CASCADE, related_name="Album")
    Cover = models.ImageField(upload_to=upload_image_path)
    Slug = models.SlugField(unique=True)

    def __str__(self):
        return self.Title


# TODO: ADD LIMITATION FOR ALBUM
# TODO: ADD MANY TO MANY FOR ARTIST

class SingleTrack(models.Model):
    Title = models.CharField(max_length=1000)
    Artist = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="SingleTrack")
    Features = models.ManyToManyField(USERSINFO, related_name="Features")
    Producers = models.CharField(max_length=1000)
    SongFile = models.FileField(validators=[Validator], upload_to=upload_song_path, unique=True)

    def __str__(self):
        return self.Title


# TODO: album works but i don't like this way I have to change manytomany to another relationship in django
def SINGLETRACK_presave(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug = unique_slug_generator(instance)


pre_save.connect(SINGLETRACK_presave, SingleTrack)
pre_save.connect(SINGLETRACK_presave, Album)
