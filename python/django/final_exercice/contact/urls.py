from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact,name='contact'),
    path('contact/',views.crud,name='crud_contact'),
    path('update_contact/<int:id>/', views.update_contact, name='update_contact'),
    path('updated_contact/<int:id>/', views.updated_contact, name='updated_contact'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    path('delted_contact/<int:id>/', views.delted_contact, name='delted_contact'),
    path('cancel_contact', views.cancel_contact, name='cancel_contact'),
        ]
