from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.model_form_view,name='model-form'),
    path('listmodelform', views.list_model_form_view,name='list-model-form'),
    path('validform', views.gmail_valid_view,name='valid-form'),
    path('addmovie', views.add_movie_view,name='add-movie'),
]



