from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Job,Employee,Salary,Location,Country,Place
# Create your views here.

def create(request):
    i = False
    if(i == False):
        i = True
        job = Job(title='developer',description='program')
        job.save()
        salary = Salary(amount=5000,extra_payment_dec=True,extra_payment_jun=True)
        salary.save()
        loacation = Location(name='rosario')
        loacation.save()
        country = Country(name='argentina',country_code='arg')
        country.save()
        place = Place(name='hostal del sol',address='santa coloma 9282',zip_code='2000',location=loacation,country=country)
        employeer = Employee(name='juan',last_name='grande',email='vale@gmail.com',job=job,salary=salary,place=place)

    query = employeer.place.country
    return HttpResponse("hello world")