from django.shortcuts import render

# Create your views here.

def optional(request, name = 'default name'):
    return render(request,'optional.html',{'name':name})