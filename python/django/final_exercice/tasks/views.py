from django.shortcuts import render
from .forms import TaskForm
# Create your views here.

def tasks(request):
    form = TaskForm()
    return render(request,'tasks.html',{'form':form})

def crud(request):
    return render(request,'crud_task.html',{})
