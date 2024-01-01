from django.shortcuts import render
from .forms import ContactForm

#Create your views here.

def contact(request):
    form = ContactForm()
    return render(request,'contact.html',{'form':form})

def crud(request):
    return render(request,'crud_contact.html',{})
