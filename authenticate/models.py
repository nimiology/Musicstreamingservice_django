from django.db import models
from .ulitis import get_filename_ext
from Songs.Ulitis import slug_genrator
from django.db.models.signals import pre_save

# Create your models here.
class USERSINFO(models.Model):
    NAME = models.CharField(max_length=1000)
    USERNAME = models.CharField(max_length=1000)
    EMAIL = models.EmailField()
    PASSWORD = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    PasswordForget = models.SlugField(unique=True)
    #PROFILEPIC = models.ImageField(upload_to=get_filename_ext,default='',blank=True)


    def __str__(self):
        return self.USERNAME

def USERINFO_presave(sender, instance, *args, **kwargs):
    status = True
    while status:
        SLUG = slug_genrator()
        qs = USERSINFO.objects.filter(PasswordForget=SLUG)
        if not qs.exists():
            SLUG = slug_genrator()
            instance.PasswordForget = SLUG
            status = False

pre_save.connect(USERINFO_presave,sender=USERSINFO)
