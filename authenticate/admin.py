from django.contrib import admin
from .models import USERINFO
class USERINFOMANAGER(admin.ModelAdmin):
    list_display = ["USERNAME","EMAIL","PASSWORD"]
# Register your models here.
admin.site.register(USERINFO,USERINFOMANAGER)