from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def admin_dash(request):
    return render(request, 'admin_dash.html')

def manageevent(request):
    return render(request, 'manageevent.html')

def is_admin(user):
    return user.is_authenticated and user.is_staff
