from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
# Create your views here.
def index(request):
    return render('template/menu/index.html')
