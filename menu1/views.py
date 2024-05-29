from django.shortcuts import render, redirect, HttpResponse

from django.conf import settings
# Create your views here.

def index(request):
    return render(request, 'runningtip/index.html')

def edit(request):
    return render(request, 'runningtip/edit.html')

def views(request):
    return render(request, 'runningtip/views.html')

<<<<<<< HEAD
def runningtip(request):
    return render(request, 'menu/runningtip.html')

def weighttip(request):
    return render(request, 'menu/weighttip.html')

def add(request):
    return render(request, 'menu/add.html')
=======
def write(request):
    return render(request, 'runningtip/write.html')
>>>>>>> d6bbcdf8ac7d6c88a329a6c773426b1e2f05cc22
