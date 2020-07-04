from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'jobtrackapp/home.html')

def login(request):
    return render(request, 'jobtrackapp/login.html')

def register(request):
    return render(request, 'jobtrackapp/register.html')

def dashboard(request):
    return render(request, 'jobtrackapp/dashboard.html')
