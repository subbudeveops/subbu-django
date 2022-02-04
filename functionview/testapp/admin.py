from django.contrib import admin
from .models import SubbuModel
# Register your models here.


class SubbuAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')


admin.site.register(SubbuModel, SubbuAdmin)
