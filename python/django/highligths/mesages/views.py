from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def mesages(request):
    messages.success(request,'hello')
    return render(request,'mesages.html',{})