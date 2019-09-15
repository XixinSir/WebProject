from django.db import models

# Create your models here.
"""写模型"""
"""有一个数据表  就有一个模型(类) 
类的属性对应表的字段"""



"""不需要设置主键   在生成时自动添加  并且值为自动增加"""
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirllnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    """如果不加这里,创建student时的sgrade会显示object"""
    def __str__(self):
        return self.gname

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    """
    在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，
    此参数为了避免两个表里的数据不一致问题，不然会报错：
    TypeError: __init__() missing 1 required positional argument: 'on_delete'


    即在外键值的后面加上 on_delete=models.CASCADE  一般为此值就好"""
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

    def __str__(self):
        return self.sname

"""
定义了模型之后,要在数据库中生成数据表:
1、生成迁移文件:
在project(根目录)下输入  python manage.py makemigrations 
在migrations目录下生成一个迁移文件,此时数据库中还没有生成数据表


2、执行迁移: 
在上面的目录下进入cmd  输入  python manage.py migrate 
相当于执行SQL语句创建数据表 表名前面加了  "项目名_"
"""




