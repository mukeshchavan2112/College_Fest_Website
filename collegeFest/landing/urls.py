from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('schedule/', views.schedule, name='schedule'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login_user'),
    path('signup', views.signup_user, name='signup_user'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
]
