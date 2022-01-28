from django.http import HttpResponse
from django.shortcuts import render
from testapp.models import Song
from testapp.forms import SongForm
from django.http import HttpResponse
# Create your views here.
def add_song_view(request):
  form=SongForm
  if request.method=="POST":
    form=SongForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('<h1>form is submite suceesfully</h1>')
  return render(request,'testapp/addsong.html',{'form':form})

def list_song_view(request):
  song_list=Song.objects.all()
  return render(request,'testapp/listsong.html',{'song_list':song_list})

