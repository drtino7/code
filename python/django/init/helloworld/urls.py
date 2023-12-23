from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sayhi/',views.sayhi,name='sayhi'),
    path('saybye/',views.saybye,name="saybye"),
    path('more_than_18/<int:age>/',views.adult ,name="more_than_18"),
]
