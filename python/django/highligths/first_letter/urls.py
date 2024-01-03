from django.urls import path
from . import views

urlpatterns = [
    path('<str:letter>/', views.first, name='first'),
]
