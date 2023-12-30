from .models import Product
from django.forms import ModelForm
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','stock']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels={
            'name': 'Product Name', 'price': 'Product Price', 'stock': 'Product Stock'
        }
        
    