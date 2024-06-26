# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.conf import settings

def index(request):
    return render(request, 'home.html')

def login(request) :
    if request.method == 'GET':
        return render(request, 'homepage/login.html');
    elif request.method == 'POST':
        username = request.POST['username'];
        password = request.POST['password'];
    
        user = auth.authenticate(request, 아이디=username, 비밀번호=password);
    
        if user is not None :
            auth.login(request, user)
            return redirect("/");
        else :
            msg = "<script>";
            msg += "alert('잘못된 계정,패스워드 입니다. 다시 로그인 하세요.');";
            msg += "location.href='/';";
            msg += "</script>";
            return HttpResponse(msg);
    

def logout(request) :
    auth.logout(request)
    return render(request, 'homepage/logged_out.html');

def createAccount(request):
    if request.method == 'GET':
        return render(request, "homepage/register.html")
    elif request.method == 'POST':
        username = request.POST.get("username");
        password = request.POST.get("password");
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        try:
            User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name);
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

    User.objects.get(username = request.user.username).delete();
    ans = "confirm('회원정보를 삭제할까요?')";

    msg = "<script>";
    msg += ans;
    if ans :
        msg += "alert('정보를 삭제합니다.')";
    else :
        msg += "alert('삭제를 취소하고 이전페이지로 돌아갑니다.')";
    msg += 'location.href="/";';
    msg += "</script>";
    return HttpResponse(msg);


def template(request):
    return render(request, 'template/')


def index(request):
    return render(request, 'menu/index.html')

def edit(request):
    return render(request, 'menu/edit.html')

def write(request):
    return render(request, 'menu/write.html')

def views(request):
    return render(request, 'menu/views.html')


