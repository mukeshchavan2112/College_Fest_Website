from django.shortcuts import render

# Create your views here.
def studentDash(request):
    return render(request, 'studentDash.html')

def eventdashboard(request):
    return render(request, 'eventdashboard.html')

def myregistration(request):
    return render(request, 'myregistration.html')

def notification(request):
    return render(request, 'notification.html')
