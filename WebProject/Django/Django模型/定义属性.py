"""
定义属性
    概述
        Django根据属性的类型确定以下信息
            当前选择的数据库支持字段的类型
            渲染管理表单时使用的默认html控件
            在管理站点最低限度的验证

        django会为表增加自动增长的主键列,每个模型只能有一个主键列,
        如果使用选项设置某属性为主键列后,则django不会再生成默认的主键列


        属性命名限制
           不能是python的保留关键字
           由于django的查询方式,不允许使用连续的下划线(一个下划线可以,但是最好不用下划线)

    库
        定义属性时,需要字段类型,字段类型被定义在django.db.models.fields目录下
        为了方便使用,被导入到django.db.models中

        使用方式
            导入from django.db import models
            通过models.Field创建字段类型的对象,赋值给属性


    逻辑删除
        对于重要数据都做逻辑删除,不做物理删除,实现方法是定义isDelete属性,类型为BooleanField,
        默认值为False
        通常
    字段类型

        AutoField
            一个根据实际ID自动增长的IntegerFied,通常不指定,如果不指定,一个主键字段将自动添加到模型中


        CharField(max_length=字符长度)
            字符串，默认的表单样式是TextInput


        TextField
            大文本字段,一般超过4000使用,默认的表单控件是Textarea


        InterField
            整数


        DecimalField(max_digits=None, decimal_places=None)
            使用python的Decimal实例表示的十进制浮点数
            参数说明
                 DedimalField.max_digits
                      位数总数
                 DecimalField.decimal_places
                      小数点后的数字位数


        FloatField
            用python的float实例来表示的浮点数


        BooleaField
            true/false字段,此字段的默认表单控件是CheckboxInput


        NullBooleanFiield
            支持null、true、false三种值



        DateField([auto_now=False,auto_now_add=False])
        使用python的datetime.date实例表示的日期
        参数说明
             DateField.auto_now
                 每次保存对象时,自动设置该字段为当前时间,用于'最后一次修改'的时间戳,它总是使用当前时间,默认为False
             DateField.auto_now_add
                 当对象第一次被创建时自动设置当前时间,用于创建的时间戳,它总是使用当前时间,默认为Fasle


        说明
             该字段默认对应的表单控件是一个TextInput,在管理员站点添加了一个Javascript写的日历控件,和一个'Today'的快捷
             按钮,包含了一个额外的invalid_date错误消息键


        注意
             auto_now_add  auto_now  auto_default这些设置是相互排斥的,他们之间的任何组合将会发生错误的结果



        TimeField
             使用Python的datetime.time实例表示的时间，参数同DateField


        DateTimeField
             使用python的datetime.datetime实例表示的时间和日期，参数同DateField


        FileField
             一个上传文件的字段


        ImageField


             继承了FileField的所有属性和方法，但对上传的对象进行校验,确保它是个有效的image


    字段选项(小括号里面的东西)

        概述
            通过字段选项,可以实现对字段的约束
            在字段对象时通过关键字参数指定

        null
            如果为True,Django将空值以NULL存储到数据库中,默认是False

        blank
            如果为True，则该字段允许为空白,默认是False

        注意: null是数据库范畴的概念,blank是表单验证范畴的

        db_column(可设置数据库字段的名称)
            字段的名称，如果未指定，则使用属性的名称

        db_index
            若值为True,则在表中会为此字段创建索引


        default
            默认值


        primary_key
            若为True,则该字段会成为模型的主键字段

        unique
            如果为True,这个字段在表中必须有唯一值


    关系
        分类
            ForeignKey:  一对多,将字段定义在多的端中
            ManyToManyField:   多对多,将字段定义在两端中
            OneToOneField:   一对一,将字段定义在任意一端中

        用一访问多
            格式
                对象.模型类小写_set
            示例
                grade.students_set

        用一访问一
            格式
                对象.模型类小写
            示例
                grade.students

        访问id
            格式
                对象.属性_id
            示例
                student.sgrade_id





"""