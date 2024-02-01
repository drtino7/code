from django.db import models

# Create your models here.

class User(models.Model):
    ussername = models.CharField(max_length=32)
    password1 = models.CharField(max_length=32)
    password2 = models.CharField(max_length=32)

    def __str__(self):
        return self.ussername
