from django.shortcuts import render, redirect, HttpResponse
from menu.models import Menu, Reply
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Max, Min, Avg, Sum
import os
from django.conf import settings
import shutil
# Create your views here.
def index(request):
    return render(request,'menu/index.html')

def running(request):
    return render(request, 'menu/running.html')

def weight(request):
    return render(request, 'menu/weight.html')

def QnA(request):
    if request.method == 'POST':
        now = datetime.now()
        menu = Menu()
        menu.제목 = request.POST['title']
        menu.내용 = request.POST.get("context");
        menu.작성자 = request.user.username;
        menu.작성일 = now
        menu.수정일 = now
        menu.조회수 = request.POST['vcount']
        menu.save()

        # file_upload(request, border.id);

        msg = "<script>";
        msg += "alert('게시글이 저장되었습니다.');";
        msg += f"location.href='/menu/QnA/{user.id}/';";
        msg += "</script>";
        return HttpResponse(msg);
    return render(request, 'menu/QnA.html')
