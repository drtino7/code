from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name','price')
    list_filter = ('name','price','stock')
    #date_hierarchy = 'date'
    


admin.site.register(Product,ProductAdmin)
