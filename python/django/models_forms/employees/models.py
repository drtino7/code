from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255,null=False)
    
    def __str__(self):
        return self.name
