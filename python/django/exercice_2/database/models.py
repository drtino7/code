from django.db import models

# Create your models here.

class Job(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

class Salary(models.Model):
    amount=models.IntegerField(null=False)
    extra_payment_dec=models.BooleanField(default=False)
    extra_payment_jun=models.BooleanField(default=False)
    def __str__(self):
        return self.Salary
class Location(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Place(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=20)
    location = models.OneToOneField(Location,on_delete=models.CASCADE)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    salary=models.ForeignKey(Salary,on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE)

    def __str__(self):
        return self.name