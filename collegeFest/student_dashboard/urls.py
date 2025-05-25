from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentDash, name='studentDash'),  # new unique name
    path('eventdashboard/', views.eventdashboard, name='eventdashboard'),
    path('myregistration/', views.myregistration, name='myregistration'),
    path('notification/', views.notification, name='notification'),
]
