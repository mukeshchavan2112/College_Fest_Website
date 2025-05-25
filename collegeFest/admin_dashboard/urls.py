from django.contrib import admin
from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.admin_dash, name='admin_dash'),
    path('manageevent/', views.manageevent, name='manageevent'),
]