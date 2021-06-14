from django.db import models
import os
from django.core.exceptions import ValidationError

def Validator(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp3','.wave']
    if not ext.lower() in valid_extensions:
        raise ValidationError('song should be MP3 or WAVE')


# Create your models here.
#TODO: Cover va song be soorat unique tolid beshan
class SingleTrack(models.Model):
    Title = models.CharField(max_length=1000)
    Artist = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    Cover = models.ImageField(upload_to=f'singleTrack/cover')
    Song = models.FileField(validators=[Validator],upload_to='singleTrack/song')


    def __str__(self):
        return self.Title