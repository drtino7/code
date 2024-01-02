from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','last_name','phone')
    search_fields = ('name','last_name','phone')
    list_filter = ('name','last_name','phone')

admin.site.register(Contact,ContactAdmin)