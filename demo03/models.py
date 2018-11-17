from django.db import models


# Create your models here.


class GroupInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    img = models.CharField(max_length=100)
    # max_digits 表示数字长度(整数位数+ 小数位数 = 长度) decimal_places 表示小数的位数
    # 现价
    current_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 原价
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    # 对应数据库的int类型
    count = models.IntegerField()
    # 假删除
    is_delete = models.BooleanField(default=False)

    #     元信息
    class Meta:
        db_table = 'group_info'


class GroupDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    end_time = models.DateTimeField()
    """
    to   对应主表类
    on_delete=None  当主表的数据删除的时候  子表如何操作关联数据
    可选值 
    models.CASCADE  cascade  (级联删除)  当主表数据删除时  子表关联数据也删除
    models.CASCADE  models.SET_NULL  当主表的记录删除时  子表关联的外键字段设为null   注意一定要在外键字段设置一下null
    models.DO_NOTHING  当主表删除数据时  子表不做任何操作
    
            
    to_field=None  参照主表的字段 默认是主表主键
    """
    # 外键的名称默认情况下  外键字段_id
    info = models.OneToOneField('GroupInfo', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'group_detail'


# ==================一对多=========================
# 主表的一条数据对应子表的多条数据
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'


class Address(models.Model):
    aid = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, related_name='addresses')

    class Meta:
        db_table = 'address'
