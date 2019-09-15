from django.db import models

# Create your models here.
class Grades(models.Model):
    class Meta:
        db_table = "grades"
        ordering = ["gname"]
    # 类里面的 属性对应表里面的字段
    gname    = models.AutoField(primary_key=True)
    ggirlnum = models.IntegerField()
    gboynum  = models.IntegerField()
    def __str__(self):
        return self.gname


class Students(models.Model):# 定义一个类方法创建对象(用@classmethod就表明是类方法)
    # cls就代表students类
    # 调用此方法就可以直接创建一个对象
    @classmethod
    def createStudent(cls, name, age, gender, contend, lastT, createT, gradeT, isD=False):
        stu = cls(sname=name, sage=age, sgender=gender,
                    scontend=contend, lastTime=lastT, createTime=createT, isDelete=isD, sgrade=gradeT)
        return stu
    # 自定义模型管理器
    # 当自定义模型管理器,objects就不存在了
    # stuObj = models.Manager()
    # stuObj2 = StudentsManger()

    sname = models.CharField(max_length=20)
    sage = models.IntegerField(db_column="age")
    scontend = models.CharField(max_length=20)
    # 关联外键
    """
        在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
        此参数为了避免两个表里的数据不一致问题，不然会报错：
        TypeError: __init__() missing 1 required positional argument: 'on_delete'


        即在外键值的后面加上 on_delete=models.CASCADE  一般为此值就好"""
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    def __str__(self):
        """
        管理站点时,创建学生时,显示的不是object,而是班级的名称
        :return:
        """
        return self.sname

    """最后一次修改的时间"""
    # lastTime = models.DateTimeField(auto_now=True)
    """创建的时间"""
    # createTime = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "students"
        ordering = ["id"]


from tinymce.models import HTMLField
class Text(models.Model):
    str = HTMLField()
