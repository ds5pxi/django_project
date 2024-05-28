from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.

def createAccount(request):
    if request.method == 'GET':
        return render(request, "homepage/register.html")
    elif request.method == 'POST':
        username = request.POST.get("username");
        password = request.POST.get("password");
        name = request.POST.get("name");
        phoneNum = request.POST.get("phoneNum");
        birth = request.POST.get("birth");
        email = request.POST.get("email");

        try:
            User.objects.create_user(username, password, name, phoneNum, birth, email);
            return redirect('/');
        except:
            msg = "<script>";
            msg += "alert('같은 아이디가 존재합니다. 다시 입력하세요.');";
            msg += "location.href='/account/register/';";
            msg += "</script>";
            return HttpResponse(msg);