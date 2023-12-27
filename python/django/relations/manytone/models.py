from django.db import models

# Create your models here.

class Reporter(models.Model):
    firs_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    date=models.DateField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    
