
from django import forms
from testapp.models import Song,Album

class SongForm(forms.ModelForm):
  class Meta:
    model=Song
    fields="__all__"

class AlbumForm(forms.ModelForm):
  class Meta:
    model=Album
    fields="__all__"

