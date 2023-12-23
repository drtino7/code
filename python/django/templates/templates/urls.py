from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/',views.template,name="template"),
    path('dinamic/<str:name>/',views.dinamic,name="dinamic")
]
