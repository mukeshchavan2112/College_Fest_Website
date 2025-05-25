from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages

# Landing Pages
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def notification(request):
    return render(request, 'notification.html')

def schedule(request):
    return render(request, 'schedule.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_dashboard:studentDash')  # this should be a named URL
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def signup_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['fullname']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=email, password=password, first_name=name)
        login(request, user)
        return redirect('student_dashboard:studentDash')  # replace with your actual dashboard URL name

    return render(request, 'signup.html')

def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard:admin_dash')
        else:
            messages.error(request, 'Invalid admin credentials or not an admin user.')
    return render(request, 'login.html')