from django import forms
from .models import Contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','last_name','phone']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'phone':forms.TextInput(attrs={'class':'form-control'}),
                }       

class Searchbar(forms.Form):
    name = forms.CharField(label='search yourn name: ', max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))