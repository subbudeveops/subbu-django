from urllib.request import HTTPCookieProcessor
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import SubbuModel
# Create your views here.
def subbu_view(request):
    now=datetime.datetime.now()
    html='time is{}'.format(now)
    return HttpResponse(html)


def list(request):
    data=SubbuModel.objects.all()
    return render(request,'testapp/listview.html',{'data':data})