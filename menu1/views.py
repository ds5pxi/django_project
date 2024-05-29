from django.shortcuts import render, redirect, HttpResponse

from django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'runningtip/index.html')

def edit(request):
    return render(request, 'runningtip/edit.html')

def views(request):
    return render(request, 'runningtip/views.html')

def write(request):
    return render(request, 'runningtip/write.html')