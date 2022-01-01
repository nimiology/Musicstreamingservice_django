from django.db import models
from .ulitis import upload_image_path
from django.contrib.auth.models import User


class UserInfo(models.Model):
    relatedName = 'userInfo'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=relatedName)
    profilePic = models.ImageField(upload_to=upload_image_path,default='profiles/DEFAULT.png')
