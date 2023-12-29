from django.shortcuts import HttpResponse
from django.shortcuts import render
from .forms import CommentForm,ContactForm
def form(request):

    commentform = CommentForm({'name':'juan','url':'http://www.google.com','comment':'hello world'})
    return render(request, 'form.html',{'commentform':commentform})

def goal(request):
    if request.method != 'POST':
        return HttpResponse('bad request')
    
    return HttpResponse(request.POST['name'])

def widget(request):
    contactform = ContactForm()
    return render(request, 'widget.html',{'form':contactform})