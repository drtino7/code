from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Publication,Article

# Create your views here.

def create(request):
    article1 = Article(headline='art1')
    article1.save()
    article2 = Article(headline='art2')
    article2.save()
    article3 = Article(headline='art3')
    article3.save()

    publication1 = Publication(title="pub1")
    publication1.save()
    publication2 = Publication(title="pub2")
    publication2.save()
    publication3 = Publication(title="pub3")
    publication3.save()
    publication4 = Publication(title="pub4")
    publication4.save()
    publication5 = Publication(title="pub5")
    publication5.save()
    publication6 = Publication(title="pub6")
    publication6.save()
    publication7 = Publication(title="pub7")
    publication7.save()

    #add

    article1.Publications.add(publication1)
    article1.Publications.add(publication2)
    article1.Publications.add(publication3)
    article2.Publications.add(publication4)
    article2.Publications.add(publication5)
    article3.Publications.add(publication6)
    article3.Publications.add(publication7)

    #pub = Publication.article_set.all()

    #remove

    article1.Publications.remove(publication1)

    query = article1.Publications.all()#filter/get/etc...



    return HttpResponse(query)
