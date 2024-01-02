from django.shortcuts import render
from .forms import TaskForm, Searchbar
from django.http import HttpResponse
from .models import Task

# Create your views here.

def tasks(request):
    form = TaskForm()
    return render(request, 'tasks.html', {'form': form})

def crud(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            search = Searchbar(request.GET)
            form.save()
            form = TaskForm()
            query = Task.objects.all()
            return render(request, 'crud_task.html', {'query': query, 'searchbar': search})
        else:
            return HttpResponse("Invalid form")
    else:
        form = TaskForm()
        return render(request, 'tasks.html', {'form': form})

def update_tasks(request, id):
    search = Searchbar(request.GET)
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form, 'task_id': id, 'searchbar': search})

def updated_tasks(request, id):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            search = Searchbar(request.GET)
            task = Task.objects.get(id=id)
            task.name = form.cleaned_data['name']
            task.date = form.cleaned_data['date']
            task.save()
            form = TaskForm()
            query = Task.objects.all()
            return render(request, 'crud_task.html', {'query': query, 'searchbar': search})
        else:
            return HttpResponse("Invalid form")
    else:
        form = TaskForm()
        return render(request, 'update_task.html', {'form': form, 'task_id': id})
    
def delete_tasks(request,id):
    search = Searchbar(request.GET)
    return render(request, 'delete_task.html', {'task_id': id, 'searchbar': search})

    
def delted_tasks(request, id):
    search = Searchbar(request.GET)
    tasks = Task.objects.get(id=id)
    tasks.delete()
    query = Task.objects.all()
    return render(request, 'crud_task.html', {'query': query, 'searchbar': search})


def cancel_tasks(request):
    query = Task.objects.all()
    search = Searchbar(request.GET)
    return render(request, 'crud_task.html', {'query': query, 'searchbar': search})


def serchbar_tasks(request):
    if request.method == 'GET':
        search = Searchbar(request.GET)
        if search.is_valid():
            query = Task.objects.filter(name__icontains=search.cleaned_data['name'])
            return render(request, 'crud_task.html', {'query': query, 'searchbar': search})