from django.urls import path
from . import views

urlpatterns = [
    path('',views.tasks,name='tasks'),
    path('tasks/',views.crud,name='crud_tasks'),
    path('update_tasks/<int:id>/', views.update_tasks, name='update_tasks'),
    path('updated_tasks/<int:id>/', views.updated_tasks, name='updated_tasks'),
    path('delete_tasks/<int:id>/', views.delete_tasks, name='delete_tasks'),
    path('delted_tasks/<int:id>/', views.delted_tasks, name='delted_tasks'),
    path('cancel_tasks', views.cancel_tasks, name='cancel_tasks'),
    path('serchbar_tasks', views.serchbar_tasks, name='serchbar_tasks'),
        ]
