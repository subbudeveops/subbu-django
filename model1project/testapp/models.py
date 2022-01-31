from distutils.command.upload import upload
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
#two wayS of validation 
def clean_images(value):
    if '.png'in value:
        raise value
    else:
        raise ValidationError('Only allowed png/jpg')
        
class SubbuModel(models.Model):
    name=models.CharField(max_length=25)
    subbu_field=models.TextField()
    marrage_image=models.ImageField(upload_to='images/') #HERE ULOADING THE IMAGES
    subbu_file=models.ImageField(upload_to='files/')# Here uloading the files
    uplaod_date=models.DateTimeField()
    updated_date=models.DateField()
    
    def __str__(self):
        return self.name
        
     