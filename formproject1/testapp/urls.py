from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form', views.Form_view,name='form1'),
    path('form1', views.Manual1_Form_view,name='manual1-form'),
    path('form2', views.Manual2_Form_view,name='initia2-form'),
    path('form3', views.Manual3_Form_view,name='manual3-form'),
    path('form4', views.Manual4_Form_view,name='manual4-form'),
    path('form5', views.Hidden_Form_view,name='manual5-form'),
    
]
