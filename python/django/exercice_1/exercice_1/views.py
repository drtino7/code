from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})
def photos(request):
    return render(request,'photos.html',{})