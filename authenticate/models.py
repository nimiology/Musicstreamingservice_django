from django.db import models
from .ulitis import get_filename_ext
# Create your models here.
class USERSINFO(models.Model):
    USERNAME = models.CharField(max_length=1000)
    EMAIL = models.EmailField()
    PASSWORD = models.CharField(max_length=1000)
    #PROFILEPIC = models.ImageField(upload_to=get_filename_ext,default='',blank=True)
    def __str__(self):
        return self.USERNAME

