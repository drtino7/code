from django.db import models

# Create your models here.a

class Contact(models.Model):
    name = models.CharField(max_length=255,null=False)
    last_name = models.CharField(max_length=255,null=False)
    phone = models.IntegerField()
    
