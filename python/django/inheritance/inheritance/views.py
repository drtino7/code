from django.shortcuts import render

def inheritance(request):
    return render(request,'inheritance.html',{})

def inheritance2(request):
    return render(request,'inheritance2.html',{})

def inheritance3(request):
    return render(request,'inheritance3.html',{})

def index(request):
    return render(request,'index.html',{})