from django.shortcuts import render, redirect 
from django.conf import settings



# Create your views here.

def index(request):
    return render(request, 'menu/index.html')

def video(request):
    return render(request, 'menu/video.html')

def aerobic(request):
    return render(request, 'menu/aerobic.html')

def arm(request):
    return render(request, 'menu/arm.html')

def back(request):
    return render(request, 'menu/back.html')

def chest(request):
    return render(request, 'menu/chest.html')

def leg(request):
    return render(request, 'menu/leg.html')

def shoulder(request):
    return render(request, 'menu/shoulder.html')

def add(request):
    return render(request, 'menu/add.html')







