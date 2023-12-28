from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('onetone/', include('onetone.urls')),
    path('manytone/',include('manytone.urls')),
    path('manytomany/',include('manytomany.urls'))
]
