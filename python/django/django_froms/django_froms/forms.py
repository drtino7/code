from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='type your name',initial='your name',max_length=100,help_text='no more than 100 characters')
    url = forms.URLField(label='your website',required=False,initial='https://')
    comment = forms.CharField()
    
class ContactForm(forms.Form):
    name = forms.CharField(label='type your name', max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='type your email', max_length=100,widget=forms.EmailInput(attrs={'class':'form-control'}))
    