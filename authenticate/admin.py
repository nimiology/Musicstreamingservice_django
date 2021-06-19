from django.contrib import admin
from .models import USERSINFO
class USERINFOMANAGER(admin.ModelAdmin):
    list_display = ["USERNAME","EMAIL","PASSWORD"]
# Register your models here.
admin.site.register(USERSINFO, USERINFOMANAGER)