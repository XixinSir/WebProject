from django.db import models

# Create your models here.
class Grades(models.Model):
    class Meta:
        db_table = "grades"
        ordering = ["gname"]
    # 类里面的 属性对应表里面的字段
    gname    = models.AutoField(primary_key=True)
    gdate    = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum  = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.gname)

class Students(models.Model):# 定义一个类方法创建对象(用@classmethod就表明是类方法)
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column="age")
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    """ 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
        此参数为了避免两个表里的数据不一致问题，不然会报错：
        TypeError: __init__() missing 1 required positional argument: 'on_delete'

        即在外键值的后面加上 on_delete=models.CASCADE  一般为此值就好"""
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    def __str__(self):
        """管理站点时,创建学生时,显示的不是object,而是班级的名称
        :return:"""
        return self.sname

    def getContend(self):
        return self.scontend

    class Meta:
        db_table = "students"
        ordering = ["id"]
