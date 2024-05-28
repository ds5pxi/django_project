
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.conf import settings

def index(request):
    return render(request, 'home.html')

def login(request) :
    return render(request, 'homepage/login.html');

def logout(request) :
    auth.logout(request);
    return render(request, 'homepage/logged_out.html');

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
            return redirect('login');
        except:
            msg = "<script>";
            msg += "alert('같은 아이디가 존재합니다. 다시 입력하세요.');";
            msg += "location.href='/account/register/';";
            msg += "</script>";
            return HttpResponse(msg);

def myinfo(request):
    user = request.user;
    userInfo = User.objects.get(username=user.username);
    content = {
        'userInfo':userInfo
    }
    if user.is_active :
        if request.method == 'GET':
            return render(request, 'hompage/myinfo.html', content);
        else:
            origin = request.POST['origin']

            if check_password(origin, user.password):
                password = request.POST.get('password');
                name = request.POST.get('name');
                phoneNum = request.POST.get('phoneNum');
                birth = request.POST.get('birth');
                email = request.POST.get('email');

                if password != None :
                    userInfo.set_password(password)
                else :
                    userInfo.set_password(origin)
                userInfo.name = name;
                userInfo.phoneNum = phoneNum;
                userInfo.birth = birth;
                userInfo.email = email;
                userInfo.save()
                
                msg = "<script>";
                msg += "alert('회원정보 수정이 완료되었습니다. 다시 로그인 하세요.');";
                msg += "location.href='account/login/';";
                msg += "</script>";
                return HttpResponse(msg);
            else:
                msg = "<script>";
                msg += "alert('비밀번호가 틀렸습니다.');";
                msg += "location.href='account/login/';";
                msg += "</script>";
                return HttpResponse(msg);
    else:
        msg = "<script>";
        msg += "alert('로그인 후 사용하세요.');";
        msg += "location.href='account/login/';";
        msg += "</script>";
        return HttpResponse(msg);

def myinfoDel(request):
    return render(request, 'homepage/myinfoDel.html');

def info(request):
    return render(request, 'template/menu/info.html')

def template(request):
    return render(request, 'template/')

def running(request):
    return render(request, 'menu/running.html')

def weight(request):
    return render(request, 'menu/weight.html')

def QnA(request):
    return render(request, 'menu/QnA.html')

