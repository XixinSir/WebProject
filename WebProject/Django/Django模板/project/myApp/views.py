from django.shortcuts import render
# Create your views here.


from .models import Students
from django.http import HttpResponse
def index(request):
    # return render(request, "myApp/index.html", {"num1": 10, "num2": 20})
    student = Students.objects.get(id=1)
    return render(request, "myApp/index.html",
           {"student": student, "num": 10, "str": "sunck is a good man",
            "list": ["good", "nice", "handsome"],
            "code": "<h1>这是h1中的内容</h1>"})


def students(request):
    list = Students.objects.all()
    return render(request, "myApp/students.html", {"students": list})


def good(request, id):
    return render(request, "myApp/good.html", {"id": id})

def main(request):
    return render(request, "myApp/main.html")

def detail(request):
    return render(request, "myApp/detail.html")

def postfile(request):
    return render(request, "myApp/postfile.html")

def showinfo(request):
    name = request.POST.get("username")
    password = request.POST.get("password")
    return render(request, "myApp/showinfo.html",
                  {"username": name, "password": password})

def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量,用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
    random.randrange(20, 100), random.randrange(20, 100))
    width = 100
    height = 50
    # 创建画面对象
    im = Image.new("RGB", (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        # 在整个范围内
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)  # 实心的点
    # 定义验证码的备选项
    str = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    # 随机选取4个值作为验证码
    rand_str = ""
    for i in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象
    font = ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf", 40)  # 大小为40
    # 构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((10, 2), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
    # 释放画笔
    del draw
    # 存入session, 用于做进一步验证
    request.session["verifycode"] = rand_str
    # 内存文件操作
    import io
    buf = io.BytesIO()  # 创建一个io流
    # 将图片保存在内存中,文件类型为png
    im.save(buf, "png")
    # 将内存中的图片数据返回给客户端,MIME类型为图片png
    from django.http import HttpResponse
    return HttpResponse(buf.getvalue(), "image/png")


def verifycodefile(request):
    flag = request.session.get("flag", True)
    str = ""
    if flag == False:
        str = "请重新输入"
    request.session.clear()
    return render(request, "myApp/verifycodefile.html", {"flag": str})


from django.shortcuts import redirect
from django.http import HttpResponseRedirect
def verifycodecheck(request):
    code1 = request.POST.get("verifycode").upper()
    code2 = request.session["verifycode"].upper()
    print("code1: ", code1)
    print("code2: ", code2)

    if code1 == code2:
        return render(request, "myApp/success.html")
    else:
        request.session["flag"] = False
        # 重定向
        # 只有一个参数
        return redirect("/sunck/verifycodefile")
