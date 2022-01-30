

from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Post(models.Model):
    Male='M'
    Female='F'
    Gender_choice=((Male,'Male'),(Female,'Female'))
    username=models.CharField(max_length=20,blank=False,null=False)
    text=models.TextField(blank=False,null=False)
    gender=models.CharField(choices=Gender_choice,max_length=6,default=Male)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
# validation model   

#creating validator function 
def validation_gmail(value):
    if '@gmail.com' in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")
        
class ValidModel(models.Model):
    gamil=models.CharField(max_length=30,validators=[validation_gmail])
    
    
    def __str__(self):
        return self.gamil
    
    
#Creating Movie Model
import re
def validation_movie(value):

    if value[0].lower!='n':
        return value
    else:
        raise ValidationError("Hero name Should be Ntr")

class MovieModel(models.Model):
    movie_name=models.CharField(max_length=20)
    relase_date=models.DateField()
    hero_name=models.CharField(max_length=20)
    heroine_name=models.CharField(max_length=20)
    director_name=models.CharField(max_length=20)
    movie_name=models.CharField(max_length=20)

    def __str__(self):
        return self.movie_name
    