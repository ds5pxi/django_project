from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'template/menu/index.html')

def template(request):
    return render(request, 'template/')

def running(request):
    return render(request, 'menu/running.html')

def weight(request):
    return render(request, 'menu/weight.html')

def QnA(request):
    return render(request, 'menu/QnA.html')