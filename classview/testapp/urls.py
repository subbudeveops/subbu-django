from django.contrib import admin
from django.urls import path
from testapp.views import subbucreate
from testapp.views import SubbuList
from testapp.views import SubbuDetail
from testapp.views import SubbuUpdate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', subbucreate.as_view()),
    path('list', SubbuList.as_view()),
    path('<pk>', SubbuDetail.as_view()),
    path('<pk>/update', SubbuUpdate.as_view()),
    path('<pk>/delete', SubbuUpdate.as_view()),
]
