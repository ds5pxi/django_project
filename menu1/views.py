from django.shortcuts import render, redirect, HttpResponse

from django.conf import settings
# Create your views here.
def info(request):
    return render(request,'menu/info.html')

def running(request):
    return render(request, 'menu/running.html')

def weight(request):
    return render(request, 'menu/weight.html')

def QnA(request):
    return render(request, 'menu/QnA.html')

def runningtip(request):
    return render(request, 'menu/runningtip.html')

def weighttip(request):
    return render(request, 'menu/weighttip.html')

def add(request):
    return render(request, 'menu/add.html')
