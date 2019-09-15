from django.conf.urls import url

"""
模板是HTML页面  可以根据视图中传递过来的数据进行填充
"""

from . import views  # 从当前文件夹中引入views文件

# 匹配到下面  执行views中index函数(视图)
"""这里才是真正匹配视图
分发
"""
urlpatterns = [
    url(r"^$", views.index),  # 什么都没有开头,什么都没有结束

    url(r"^(\d+)/(\d+)/$", views.detail),

    url(r"^grades/$", views.grades),  # 此url匹配到此视图了

    url(r"^students/$", views.students),

    url(r"^grades/(\d+)$", views.gradeStudents)

]
# 以数字开头 以$结尾  (\d+)用来接收数值  一定要加括号

