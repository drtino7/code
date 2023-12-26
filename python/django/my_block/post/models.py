from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=5)

    author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline