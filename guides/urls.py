from django.urls import path
from . import views

urlpatterns = [
    path('', views.guide_list, name='guide-list'),
    path('featured/', views.guide_featured, name='guide-featured'),
    path('<int:pk>/', views.guide_detail, name='guide-detail'),
]
