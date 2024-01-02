from django.urls import path
from . import views

urlpatterns = [
    path('', views.mesages, name='mesages'),
]
