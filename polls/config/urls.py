from django.urls import path
from django.urls import include
from django.contrib import admin
from rest_framework import routers

urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('admin/', admin.site.urls),
]
