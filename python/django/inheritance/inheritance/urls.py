from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inheritance/',views.inheritance, name="inheritance"),
    path('inheritance2/',views.inheritance2, name="inheritance2"),
    path('inheritance3/',views.inheritance3, name="inheritance3"),
    path('index/',views.index,name="index")
]
