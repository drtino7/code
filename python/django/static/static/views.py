from django.shortcuts import render

def static(request):
    return render(request,'static.html',{})