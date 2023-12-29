from django.shortcuts import render
from django.shortcuts import HttpResponse
def forms(request):
    return render(request,'forms.html',{})

def get_goal(request):
    if request.method != 'GET':
        return HttpResponse('method post is not supported')
    
    name = request.GET['name']
    return render(request,'goal.html',{'name':name})

def post_form(request):
    return render(request,'post_foms.html',{})


def post_goal(request):
    if request.method != 'POST':
        return HttpResponse('method get is not supported')
    info = request.POST['info']
    return render(request,'goal_post.html',{'info':info})



        
    
