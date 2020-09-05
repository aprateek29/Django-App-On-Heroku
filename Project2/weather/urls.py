from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<pk>/', views.deleteCity, name='delete'),
]