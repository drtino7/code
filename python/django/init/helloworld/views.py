from django.http import HttpResponse

def sayhi(request):
    return HttpResponse("hello world")

def saybye(request):
    return HttpResponse("bye")

def adult(request,age):
    if(age >= 18):
        return HttpResponse("you are an adult")
    else:
        return HttpResponse("you are not an adult")