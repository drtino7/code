from django import forms
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','date']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}), 'date':forms.DateInput(attrs={'class':'form-control'})
        }
