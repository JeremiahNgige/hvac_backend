"""hvacapi URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/categories/', include('categories.urls')),
    path('api/guides/', include('guides.urls')),
    path('api/tips/', include('tips.urls')),
]
