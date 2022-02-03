from turtle import title
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def clean(self):
    if len(title)<2:
        raise ValidationError('Shouldbe minimum 2 ')
    return title
    

class SubbuModel(models.Model):
    title=models.CharField(max_length=100,validators=[clean])
    desc=models.TextField()
    
    
    def __str__(self):
        return self.title