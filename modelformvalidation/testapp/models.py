from django.db import models

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
