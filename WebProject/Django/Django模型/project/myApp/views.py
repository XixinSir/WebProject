from django.shortcuts import render

# Create your views here.
from .models import Students, Grades
from django.http import HttpResponse


# 输入students对应的视图
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request, "myApp/students.html",
                  {"students": studentsList})

def students2(request):
    # 报异常
    studentsList = Students.stuObj2.get(sgender=True)
    return HttpResponse("----------------------------------")


# 显示前5条学生
def students3(request):
    # 报异常
    studentsList = Students.stuObj2.all()[0:2]
    return render(request, "myApp/students.html",
                  {"students": studentsList})


# 分页显示学生
def stupage(request, page):
    #  0-5   5-10   10-15
    #   1     2       3
    #  page * 5
    page = int(page)
    studentsList = Students.stuObj2.all()[(page - 1) * 5: page * 5]
    return render(request, "myApp/students.html",
                  {"students": studentsList})


from django.db.models import Max
# 输入students对应的视图
def studentssearch(request):
    # 注意是两个下划线
    # studentsList = Students.stuObj2.filter(sname__contains="刘德华")
    # studentsList = Students.stuObj2.filter(sname__endswith="1")
    # studentsList = Students.stuObj2.filter(id__in=[1, 2, 5])
    # studentsList = Students.stuObj2.filter(sage__gt=20)
    # studentsList = Students.stuObj2.filter(lastTime__year=2019)
    # studentsList = Students.stuObj2.filter(sname__contasins="刘%")  # 匹配刘%

    # 描述中带有张柏芝这三个字的数据是属于哪个班级的
    grade = Grades.objects.filter(students__scontend__contains='张柏芝')
    print(grade)

    studentsList = Students.stuObj2.filter(Q(id__lte=3))
    # studentsList = Students.stuObj2.filter(Q(sage__gt=10) | Q(id__lte=3))
    # studentsList = Students.stuObj2.filter(~Q(id__lte=3))


    return render(request, "myApp/students.html",
                  {"students": studentsList})



def index(request):
    return HttpResponse("sunck is a good man")


def addstudent(request):
    grade = Grades.objects.get(gname=1101)
    stu = Students.createStudent("刘德华", 23, True, "I am liudehua",
                                 "2019-07-21 17:32:23",  "2019-07-21 17:32:23", grade)
    stu.save()
    return HttpResponse("Are you OK")



def addstudent2(request):
    grade = Grades.objects.get(gname=1101)
    stu = Students.stuObj2.creatStudent("刘德华111", 23, True, "I am liudehua1111",
                                 "2019-07-21 17:32:23",  "2019-07-21 17:32:23", grade)
    stu.save()
    return HttpResponse("*************************")

from django.db.models import F,Q
def grades(request):
    # g = Grades.objects.filter(ggirlnum__gt=F("gboynum")+15)
    # # 如果print要把 定义模型类的  def __str__(self): return self.gname  注释掉  以免出现类型转换错误
    # print(g)

    return HttpResponse("65768sfddf7")
