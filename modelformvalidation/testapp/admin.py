from django.contrib import admin
from .models import Post,ValidModel,MovieModel
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['username','text','gender','time']
admin.site.register(Post,PostAdmin)

# VallidModel register inside admin.py
admin.site.register(ValidModel)


admin.site.register(MovieModel)
