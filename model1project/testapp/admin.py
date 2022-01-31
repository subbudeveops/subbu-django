from django.contrib import admin
from testapp.models import SubbuModel

# Register your models here.
class SubbuModelAdmin(admin.ModelAdmin):
    list_display=('name','subbu_field','marrage_image','subbu_file','uplaod_date','updated_date')
admin.site.register(SubbuModel,SubbuModelAdmin)