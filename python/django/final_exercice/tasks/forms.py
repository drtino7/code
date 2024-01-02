from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','date']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}), 'date':forms.DateInput(attrs={'class':'form-control'})
        }


class Searchbar(forms.Form):
    name = forms.CharField(label='search yourn name: ', max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
