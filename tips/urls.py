from django.urls import path
from . import views

urlpatterns = [
    path('', views.tip_list, name='tip-list'),
    path('featured/', views.tip_featured, name='tip-featured'),
    path('<int:pk>/', views.tip_detail, name='tip-detail'),
]
