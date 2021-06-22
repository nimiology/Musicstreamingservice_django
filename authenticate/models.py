from django.db import models
from .ulitis import get_filename_ext
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model

# Create your models here.
class USERSINFO(models.Model):
    NAME = models.CharField(max_length=1000)
    USERNAME = models.CharField(max_length=1000)
    EMAIL = models.EmailField()
    PASSWORD = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    #PROFILEPIC = models.ImageField(upload_to=get_filename_ext,default='',blank=True)


    def __str__(self):
        return self.USERNAME

def USERINFO_presave(sender, instance, *args, **kwargs):
    USER  = get_user_model()
    USER.objects.create_user(username=instance.USERNAME, password=instance.PASSWORD,email=instance.EMAIL)

pre_save.connect(USERINFO_presave,sender=USERSINFO)
