from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry,Author

# Create your views here.

def queries(request):
    #get all
    Authors = Author.objects.all()
    #filter
    Author_filteres = Author.objects.filter(email='nruiz@example.com')
    #get one
    author = Author.objects.get(id=1)
    #limit
    limit = Author.objects.all()[:10]
    #get 5 values skiping 5 first
    skip = Author.objects.all()[5:10]
    #order by
    Authors = Author.objects.all().order_by('email')
    #
    #__lte menor than equal
    #__gte greater than equal
    #__gt greater than
    #__lt less than
    #__contains contain
    #__exact exact
    filterer = Author.objects.filter(id__lte=15)
    #author who has in his name the word yes
    author_yes = Author.objects.filter(name__contains='yes')

    return render(request,'post.html',{'Authors':Authors,'filter':Author_filteres,'aut':author,'limit':limit,'skip':skip})

def update(request):
    author = Author.objects.get(id=1)
    author.name='juan'
    author.email='j@j.com'
    author.save()
    return HttpResponse('updated')