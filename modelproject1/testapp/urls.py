from django.contrib import admin
from django.urls import path
from testapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addsong', views.add_song_view,name='add_song'),
    path('listsong', views.list_song_view,name='list_song'),
]