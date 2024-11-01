# bot/urls.py
from django.urls import path
from .views import index,loading,homepage

urlpatterns = [
    path('',homepage,name='homepage'),
    path('index', index, name='index'),
    path('loading',loading,name="loading")
]
