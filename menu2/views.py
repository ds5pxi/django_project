from django.shortcuts import render, redirect, HttpResponse

from django.conf import settings
# Create your views here.
def arm(request):
    return render(request,'menu/arm.html')

def back(request):
    return render(request, 'menu/back.html')

def chest(request):
    return render(request, 'menu/chest.html')

def legs(request):
    return render(request, 'menu/legs.html')

def shoulder(request):
    return render(request, 'menu/shoulder.html')

def aerobic(request):
    return render(request, 'menu/aerobic.html')
