from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks,name='tasks'),
    path('tasks/',views.crud,name='crud'),
        ]
