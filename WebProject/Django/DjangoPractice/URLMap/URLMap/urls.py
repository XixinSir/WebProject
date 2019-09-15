"""URLMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url


"""

urlpatterns列表中增加了一个路径app/,将其转接到app.urls包,即URLMap/app/urls.py文件
^app/  所有以app开头的路由


启用服务器后可通过浏览器访问http://127.0.0.1:8000/app/ 检验欢迎消息

"""
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r"^app/", include("app.urls")),
]
