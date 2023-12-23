from django.shortcuts import render

def template(request):
    return render(request,'templates.html',{})

def dinamic(request,name):
    categories = ['python','java','c++']
    context = {'name' : name,'categories':categories}
    return render(request,'dinamic.html',context)
