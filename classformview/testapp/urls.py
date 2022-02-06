from django.contrib import admin
from django.urls import path
from testapp.views import SubbuFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',SubbuFormView.as_view())
]