from unittest.util import _MAX_LENGTH
from django.db import models
from traitlets import default

# Create your models here.

class Coment(models.Model):

    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    coment = models.TextField(max_length=1000, null=False)
    date = models.DateField(null=True)

class product(models.Model):
    name = models.CharField(max_length=255,null=False)
    value = models.IntegerField(null=False)


    def __str__(self):
        return self.name
    
