from django.contrib import admin
from .models import Task
# Register your models here.





class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    search_fields = ('name','date')
    list_filter = ('name','date')



admin.site.register(Task,TaskAdmin)

