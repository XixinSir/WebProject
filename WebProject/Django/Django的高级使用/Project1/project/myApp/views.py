from django.shortcuts import render

# Create your views here.
from .models import Students, Grades
from django.http import HttpResponse


def index(request):
    return render(request, "myApp/index.html")

# 上传文件
def upfile(request):
    return render(request, "myApp/upfile.html")
# 把上传的文件拿出来
import os
from django.conf import settings
def savefile(request):
    # 需要是POST请求
    if request.method == "POST":
        # input的name为file
        f = request.FILES["file"]
        # 文件在服务器端的路径
        filePath = os.path.join(settings.MEDIA_ROOT, f.name)
        with open(filePath, "wb") as fp:
            # 文件大 一部分一部分上传
            for info in f.chunks():
                fp.write(info)
        return HttpResponse("上传成功")
    else:
        return HttpResponse("上传失败")


from .models import Students
from django.core.paginator import Paginator
def studentpage(request, pageid):
    # 所有学生列表
    allList = Students.objects.all()
    # 每6条为一页
    paginator = Paginator(allList, 6)
    # 每次拿一页
    page = paginator.page(pageid)
    return render(request, "myApp/studentpage.html",{"students": page})


def ajaxstudents(request):
    return render(request, "myApp/ajaxstudents.html")
# ajax
from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.objects.all()
    list = []
    for stu in stus:
        list.append([stu.sname, stu.sage, stu.scontend])
    return JsonResponse({"data": list})


def edit(request):
    return render(request, "myApp/edit.html")

import time
def celery(request):
    print("sunck is a good man")
    time.sleep(5)
    print("sunck is a nice man")
    return render(request, "myApp/celery.html")