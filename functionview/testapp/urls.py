from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createview', views.creative_view),
    path('listview', views.list_view),
    path('<id>',views.detail_view),
    path('<id>/update',views.update_view),
    path('<id>/delete',views.delete_view),
]
