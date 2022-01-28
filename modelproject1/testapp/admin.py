from django.contrib import admin
from .models import Album,Song
# Register your models here.
class SongAdmin(admin.ModelAdmin):
  list_display=['name','album']
admin.site.register(Song,SongAdmin)


class AlbumAdmin(admin.ModelAdmin):
  list_display=['title','artist','genre']
admin.site.register(Album,AlbumAdmin)