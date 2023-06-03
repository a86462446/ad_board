from django.contrib import admin
from .models import Video

# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ("videoname", "add_date")

admin.site.register(Video, VideoAdmin)