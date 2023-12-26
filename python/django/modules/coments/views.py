from django.http import HttpResponse
from django.shortcuts import render
from .models import Coment

# Create your views here.

def test(request):
    return HttpResponse("hello world")

def create(request):
    #coment = Coment(name="juan",score="7",coment="hello world")
    #coment.save()
    coment = Coment.objects.create(name="luis",score="4",coment="hello")
    return HttpResponse("hello world")

def delete(request):
    name_user = "juan"
    #coment = Coment.objects.get(id=1)
    #coment = Coment.objects.get(name=name_user)
    #coment.delete()
    Coment.objects.filter(id=2).delete()
    return HttpResponse(f"user: {name_user} has been deleted ")