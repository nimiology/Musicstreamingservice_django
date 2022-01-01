from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from .Ulitis import Validator, upload_album_cover_path, upload_song_path, upload_playlist_cover_path, slug_genrator
from Users.models import UserInfo


class Album(models.Model):
    relatedName = 'albums'

    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name=relatedName)
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=512, null=True, blank=True)
    cover = models.ImageField(upload_to=upload_album_cover_path)
    createDTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.artist.username} - {self.title}'


class Track(models.Model):
    relatedName = 'tracks'

    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name=relatedName)
    title = models.CharField(max_length=1000)
    slug = models.SlugField(blank=True, unique=True, max_length=102)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name=relatedName)
    feature = models.ManyToManyField(User, blank=True, related_name='featurings')
    songFile = models.FileField(validators=[Validator], upload_to=upload_song_path)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.artist.username} - {self.title}'


class Playlist(models.Model):
    relatedName = 'playlists'
    defaultPic = 'Playlist/cover/DEFAULT.png'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name=relatedName)
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=512, unique=True, blank=True)
    cover = models.ImageField(upload_to=upload_playlist_cover_path, default=defaultPic, blank=True, null=True)
    tracks = models.ManyToManyField(Track, blank=True, related_name=relatedName)
    createdTime = models.DateTimeField(auto_now_add=True)
    lastEdit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.title}'


def slug_pre_save(sender, instance, *args, **kwargs):
    if not instance.Slug:
        slug = slug_genrator()


pre_save.connect(slug_pre_save, sender=Track)
pre_save.connect(slug_pre_save, sender=Album)
pre_save.connect(slug_pre_save, sender=Playlist)
