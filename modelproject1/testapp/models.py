from tkinter import CASCADE
from django.db import models

# Create your models here.
class Album(models.Model):
  
  title=models.CharField(max_length=15)
  artist=models.CharField(max_length=15)
  genre=models.CharField(max_length=30)


  def __str__(self):
    return self.title

class Song(models.Model):
  album=models.ForeignKey(Album,on_delete=models.CASCADE)
  name=models.CharField(max_length=50)



