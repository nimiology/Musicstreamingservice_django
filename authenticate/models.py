from django.db import models

# Create your models here.
class USERINFO(models.Model):
    USERNAME = models.CharField(max_length=1000)
    EMAIL = models.EmailField()
    PASSWORD = models.CharField(max_length=1000)
    def __str__(self):
        return self.USERNAME

