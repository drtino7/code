from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Reporter,Article
from datetime import date
# Create your views here.

def create(request):
    reporter=Reporter(firs_name="juan",last_name="perez",email="hello@example.com")
    reporter.save()
    article1 = Article(headline="art1",date=date(2022,5,5),reporter=reporter)
    article1.save()
    article2 = Article(headline="art2",date=date(2022,7,3),reporter=reporter)
    article2.save()
    article3 = Article(headline="art3",date=date(2021,2,12),reporter=reporter)
    article3.save() 

    #query = article1.reporter.last_name
    #query = reporter.article_set.all()
    #query = reporter.article_set.filter(headline="art1")
    query = reporter.article_set.count()
    return HttpResponse(query)
