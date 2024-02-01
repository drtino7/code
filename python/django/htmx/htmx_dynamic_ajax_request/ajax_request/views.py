from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse

# Create your views here.

def ajax_request(request):
    form = UserForm()
    return render(request,'ajax_request.html',{'form':form})

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div style='color:red;'>the username already exists</div>")
    else:
        return HttpResponse("<div style='color:green;'>the username is valid</div>")

def check_password1(request):
    password1 = request.POST.get('password1')
    if len(password1) < 8:
        return HttpResponse("<div style='color:red'>password should have more than 8 caracters</div>")
    else:
        return HttpResponse("<div style=''color:green>password is correct</div>")





def check_password2(request):
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 != password2:
        return HttpResponse("<div style='color:red'>password not concide</div>")
    else:
        return HttpResponse("")
        
