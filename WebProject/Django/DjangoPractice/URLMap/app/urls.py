
"""用来管理应用app中的所有URL映射"""


"""Django中的所有映射由该函数生成"""
from django.conf.urls import url
"""从app目录里面引入views.py模块"""
from . import views

"""本例中把所有路由映射到view.py中的welcome函数"""
urlpatterns = {
    url(r"", views.welcome),
}