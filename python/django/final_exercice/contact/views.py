from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def crud(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            query = Contact.objects.all()
            return render(request, 'crud_contact.html', {'query': query})
        else:
            return HttpResponse("Invalid form")
    else:
        form = ContactForm()
        return render(request, 'crud_contact.html', {'form': form})

def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(instance=contact)
    return render(request, 'update_contact.html', {'form': form, 'contact_id': id})

def updated_contact(request, id):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Updating info
            contact = Contact.objects.get(id=id)
            contact.name = form.cleaned_data['name']
            contact.last_name = form.cleaned_data['last_name']
            contact.phone = form.cleaned_data['phone']
            contact.save()
            form = ContactForm()
            query = Contact.objects.all()
            return render(request, 'crud_contact.html', {'query': query})
        else:
            return HttpResponse("Invalid form")
    else:
        form = ContactForm()
        return render(request, 'update_contact.html', {'form': form, 'contact_id': id})
    
def delete_contact(request,id):
    return render(request, 'delete_contact.html', {'contact_id': id})

    
def delted_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    query = Contact.objects.all()
    return render(request, 'crud_contact.html', {'query': query})


def cancel_contact(request):
    query = Contact.objects.all()
    return render(request, 'crud_contact.html', {'query': query})