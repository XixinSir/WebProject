from django.contrib import admin

# Register your models here.

"""
admin站点管理(提供一个可视化界面来管理数据):
     内容发布:负责添加、修改、删除内容(数据库的数据)
     公告访问: 
     
     
------
需要在settings.py中配置Admin应用
(在INSTALLED_APPS中添加django.contrib.admin)(默认已配置)


------创建管理员用户
进入project目录
python manage.py createsuperuser 
http://127.0.0.1:8000/admin 可以进入登录界面

-----汉化
修改settings.py文件
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'


-----管理数据表
修改admin.py文件
admin.site.register(Grades) 
admin.site.register(Students)  进行注册


-----自定义管理页面

"""
from .models import Grades, Students

# 也可继承自admin.StackedInline 但是页面显示没有下面的好看
class StudentsInfo(admin.TabularInline):
    model = Students  # 用Students的模型
    extra = 2  # 创建2个

class GradesAdmin(admin.ModelAdmin):
    """加到register方法里面才有用"""
    """列表页属性"""

    """创建班级时就创建几个学生"""
    inlines = [StudentsInfo]  # 加2个

    # 显示字段  想显示什么就写什么字段
    list_display = ["id", "gname", "gdate", "ggirllnum", "gboynum", "isDelete"]

    # 过滤字段 可以写多个
    list_filter = ["gname", "gdate"]

    # 搜索字段 可写多个
    search_fields = ["gname", "ggirllnum"]

    # 分页 每n条是一页
    list_per_page = 20

    """添加、修改页属性  fields和fieldsets不能同时使用"""
    # fields数据显示顺序  id不可以写(id不可以添加)
    # fields = ["ggirllnum", "gboynum", "isDelete", "gname", "gdate"]
    # fieldsets 给属性分组
    fieldsets = [
        ("num",  {"fields": ["ggirllnum", "gboynum"]}),
        ("base", {"fields": ["isDelete", "gname", "gdate"]})
    ]


# 将注册换成用装饰器来注册
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 注意 这里显示的是sgrade不是sgrade_id

    """布尔值显示问题"""
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    # 设置页面列的名称 写函数
    gender.short_description = "性别"

    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True


    # list_display = ["id", "sname", "sgender", "sage", "scontend", "isDelete", "sgrade"]
    """将布尔值转换为男女"""
    list_display = ["id", "sname", gender, "sage", "scontend", "isDelete", "sgrade"]

# 注册
admin.site.register(Grades, GradesAdmin)
# admin.site.register(Students, StudentsAdmin)
