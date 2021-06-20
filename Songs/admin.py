from django.contrib import admin
from .models import SingleTrack,Album

class SingleTrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ['Title']}

admin.site.register(SingleTrack,SingleTrackAdmin)
admin.site.register(Album,SingleTrackAdmin)
