from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request) :
    return render(request, 'main.html');

def login(request) :
    return render(request, 'login.html');

def logout(request) :
    return render(request, 'logout.html');

def createAccount(request):
    return render(request, 'creaateAccount');

def myinfo(request):
    return render(request, 'myinfo.html');

def myinfoDel(request):
    return render(request, 'myinfoDel');