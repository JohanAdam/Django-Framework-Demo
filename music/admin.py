from django.contrib import admin
from .models import Album, Song

# Register your models here.

#Add new category
admin.site.register(Album)
admin.site.register(Song)
