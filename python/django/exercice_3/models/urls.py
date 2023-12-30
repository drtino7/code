from django.urls import path
from . import views

urlpatterns = [
    path('',views.insert,name="insert"),
    path('inserted/',views.inserted,name="inserted"),
]
