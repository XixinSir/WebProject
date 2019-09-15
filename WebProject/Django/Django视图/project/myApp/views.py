from django.shortcuts import render
# Create your views here.
from .models import Students, Grades
from django.http import HttpResponse
def index(request):
    return render(request, "myApp/index.html")
    # return HttpResponse("sunck is a good man")
def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")
# 获取get传递的数据
def get1(request):
    a = request.GET.get("a")
    b = request.GET["b"]
    c = request.GET.get("c")
    return HttpResponse(a + "   " + b + "  " + c)

def get2(request):
    a = request.GET.getlist("a")
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get("c")
    return HttpResponse(a1 + "   " + a2 + "  " + c)
# POST
def showregist(request):
    return render(request, "myApp/regist.html")
def regist(request):
    # 标签里面的name属性就是传回来的键值
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse("soaf")
# response
def showresponse(request):
    res = HttpResponse()
    res.content = b"good"
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res
# cookie
def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>" + cookie["sunck"] + "</h1>")
    # cookie = res.set_cookie("sunck", "good")
    return res
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
# 重定向
def redirect1(request):
    return redirect("/redirect2")
    # return HttpResponseRedirect("/redirect2")
def redirect2(request):
    return HttpResponse("我是重定向后的视图")
# session
def main(request):
    # 取session   找到就返回name的对应的键值 找不到返回"游客"
    username = request.session.get("name", "游客")
    print(username)
    return render(request, "myApp/main.html", {"username": username})
def login(request):
    return render(request, "myApp/login.html")
def showmain(request):
    print("*****************")
    # 获取表单提交的数据 username就是输入的值
    username = request.POST.get("username")
    print("username=", username)
    # 存储session
    request.session["name"] = username
    # 10s过期
    # request.session.set_expiry(10)
    return redirect("/main")
from django.contrib.auth import logout
def quit(request):
    # 清除session  推荐logout
    logout(request)
    # request.session.clear()
    # request.session.flush()
    return redirect("/main")

