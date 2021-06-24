from django.db import models
from .ulitis import get_filename_ext
from Songs.Ulitis import slug_genrator
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
class USERSINFO(models.Model):
    NAME = models.CharField(max_length=1000)
    USERNAME = models.CharField(max_length=1000,unique=True)
    EMAIL = models.EmailField(unique=True)
    PASSWORD = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True)
    PasswordForget = models.SlugField(unique=True)
    #PROFILEPIC = models.ImageField(upload_to=get_filename_ext,default='',blank=True)
    CREATE = models.BooleanField(default=False)


    def __str__(self):
        return self.USERNAME

def USERINFO_presave(sender, instance, *args, **kwargs):
    if instance.CREATE:
        #create user
        USER = get_user_model()
        USER.objects.create_user(username=instance.USERNAME, password=instance.PASSWORD,email=instance.EMAIL)
    else:
        u = User.objects.get(username=instance.USERNAME)
        u.set_password(instance.PASSWORD)
        u.save()
    #forget password
    status = True
    while status:
        SLUG = slug_genrator()
        qs = USERSINFO.objects.filter(PasswordForget=SLUG)
        if not qs.exists():
            SLUG = slug_genrator()
            instance.PasswordForget = SLUG
            status = False
    #slug
    instance.Slug = instance.USERNAME

pre_save.connect(USERINFO_presave,sender=USERSINFO)
