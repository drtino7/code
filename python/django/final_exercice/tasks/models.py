from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255,null=False)
    date = models.DateField()
