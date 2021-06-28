from django.db import models
from django.db.models.signals import pre_save
from .Ulitis import Validator, upload_album_cover_path, upload_song_path, upload_playlist_cover_path, slug_genrator
from Users.models import USERSINFO

class Playlist(models.Model):
    Title = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True, blank=True, max_length=102)
    Owner = models.ForeignKey(USERSINFO, on_delete=models.CASCADE, related_name='Owner')
    Cover = models.ImageField(upload_to=upload_playlist_cover_path, default='Playlist/cover/DEFAULT.png', blank=True)
    CreatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Title']

    def __str__(self):
        return self.Title


class Album(models.Model):
    Title = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True, max_length=102)
    Artist = models.ForeignKey(USERSINFO, on_delete=models.CASCADE, related_name="Album")
    Cover = models.ImageField(upload_to=upload_album_cover_path)
    CreateDTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Title']

    def __str__(self):
        return self.Title


class SingleTrack(models.Model):
    Title = models.CharField(max_length=1000)
    Slug = models.SlugField(blank=True, unique=True, max_length=102)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="SingleTrack")
    Features = models.ManyToManyField(USERSINFO, related_name="Features", blank=True)
    SongFile = models.FileField(validators=[Validator], upload_to=upload_song_path, unique=True)
    AddedToPlaylist = models.ManyToManyField(Playlist,related_name='Songs',blank=True)
    CreatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Title']

    def __str__(self):
        return self.Title





def SingleTrack_SLUG_presave(sender, instance, *args, **kwargs):
    if instance.Slug == '':
        status = True
        while status:
            SLUG = slug_genrator()
            qs = SingleTrack.objects.filter(Slug=SLUG)
            if not qs.exists():
                instance.Slug = SLUG
                status = False


def Album_SLUG_presave(sender, instance, *args, **kwargs):
    if instance.Slug == '':
        status = True
        while status:
            SLUG = slug_genrator()
            qs = Album.objects.filter(Slug=SLUG)
            if not qs.exists():
                instance.Slug = SLUG
                status = False


def Playlist_SLUG_presave(sender, instance, *args, **kwargs):
    if instance.Slug == '':
        status = True
        while status:
            SLUG = slug_genrator()
            qs = Playlist.objects.filter(Slug=SLUG)
            if not qs.exists():
                instance.Slug = SLUG
                status = False


pre_save.connect(SingleTrack_SLUG_presave, sender=SingleTrack)
pre_save.connect(Album_SLUG_presave, sender=Album)
pre_save.connect(Playlist_SLUG_presave, sender=Playlist)
