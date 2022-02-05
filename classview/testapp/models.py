from django.db import models

# Create your models here.


class SubbuModel(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.title


class ListModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
