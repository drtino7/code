from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.shortcuts import HttpResponse
from .models import Product
# Create your views here.



def insert(request):
        form = ProductForm()
        return render(request,'index.html',{'form':form})

def inserted(request):
        
        if request.method != 'POST':
            return HttpResponse('bad request')
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                #form.save()
                Product.objects.create(name=request.POST['name'],price=request.POST['price'],stock=request.POST['stock'])
                products = Product.objects.filter(name=request.POST['name'])
                price = Product.objects.get(id=1).price

                products[0].price

                return render(request,'inserted.html',{'products':products[0].name})
            else:
                return HttpResponse('bad request')
                 