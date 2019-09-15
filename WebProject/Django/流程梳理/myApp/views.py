from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

"""写视图

在django中,视图对web请求进行回应
视图就是一个python函数,在views.py文件中定义"""

# reqest请求体  浏览器给服务器的东西
def index(reqest):
    return HttpResponse("sunck is a good man")

def detail(request, num, num2):
    return HttpResponse("detail-%s-%s" % (num, num2))

from .models import Grades, Students
def grades(request):
    # 去模型里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板 模板再渲染页面 将渲染好的 页面返回浏览器
    # 路径和settings.py里的DIRS进行拼接
    return render(request, "myApp/grades.html",
                  {"grades": gradesList})  # 用ggradesList取代模板中的grades

def students(request):
    studentsList = Students.objects.all()
    return render(request, "myApp/students.html",
                  {"students": studentsList})  # 用studentsList取代模板中的studentsList

def gradeStudents(request, num):
    grade = Grades.objects.get(id=num)
    studentsList = grade.students_set.all()
    return render(request, "myApp/students.html",
                  {"students": studentsList})

