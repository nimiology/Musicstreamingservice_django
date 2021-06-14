from django.contrib import admin
from .models import SingleTrack

class SingleTrackAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug': ['Title','Artist']}

# Register your models here.
admin.site.register(SingleTrack,SingleTrackAdmin)