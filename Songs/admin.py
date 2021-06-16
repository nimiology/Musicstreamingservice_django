from django.contrib import admin
from .models import SingleTrack,Album

class SingleTrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ['Title','Artist']}

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ['Title','Artist']}
# Register your models here.
admin.site.register(SingleTrack,SingleTrackAdmin)
admin.site.register(Album,AlbumAdmin)
