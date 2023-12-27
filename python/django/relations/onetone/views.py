from django.shortcuts import render
from django.http import HttpResponse
from .models  import Place,Restaurant
# Create your views here.

def create(request):
    place = Place(name="place 1",address="address 1")
    place.save()
    restaurant=Restaurant(place=place,number_of_employees=7)
    restaurant.save()


    return HttpResponse(restaurant.place.name)