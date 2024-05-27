from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request) :
    return render(request, 'main.html');

def login(request) :
    return render(request, 'registeration/login.html');

def logout(request) :
    return render(request, 'registeration/logged_out.html');

def createAccount(request):
    return render(request, 'registeration/login.html');

def myinfo(request):
    return render(request, 'registeration/myinfo.html');

def myinfoDel(request):
    return render(request, 'registeration/myinfoDel');