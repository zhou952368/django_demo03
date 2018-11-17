import datetime
from demo03.models import *
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# 增删改查操作
# 注意 主表添加数据跟单表操作一样 往子表添加数据的时候 主表数据一定要存在


def add(request):
    info = GroupInfo(title='佳欢小姐姐',
                     img='/static/img/',
                     current_price=99.00,
                     original_price=998.00,
                     count=50)
    info.save()
    # 子表外键字段 可以设置对象 也可以设置主键
    detail = GroupDetail(description='白天么么哒,晚上啪啪啪!!!',
                         end_time=datetime.datetime.strptime('2018-11-16 18:20:20', '%Y-%m-%d %H:%M:%S'),
                         info_id=info.info_id)
    detail.save()
    return HttpResponse('一对一添加数据')


"""
正向查询   通过子表模型查询主表
反向查询   通过主表模型查询子表
"""


def find(request):
    # 通过子表模型查询主表数据
    detail_list = GroupDetail.objects.all()
    for detail in detail_list:
        print(detail.description)
        # 如果想获取主表的数据   可以直接通过子表的外键属性获取主表的相关信息
        print(detail.info.title)
    return render(request, 'shops.html', context={'detail': detail_list})


def find1(request):
    infos = GroupInfo.objects.all()
    # 如果想通过主表模型获取子表相关信息
    # 语法:  主表模型对象.子表模型类名小写
    for info in infos:
        print(info.title)
        print(info.groupdetail.description)
    return HttpResponse('通过主表获取子表数据')


def add1(request):
    user = User(name="zja")
    user.save()
    # 批量添加
    li = [Address(desc=f'武汉市高新区金融港智慧园{i}', user_id=user.uid) for i in range(1, 11)]
    Address.objects.bulk_create(li)
    return HttpResponse('一对多添加')


"""
正向查询   跟一对一一样
反向查询  
"""


# 一对一情况下 主表对象.从表模型名小写_set
def fk_find(request):
    # address_list = Address.objects.all()
    # address_list[1].user.name

    # 推荐使用
    # user = User.objects.get(uid=1)
    # address = user.address_set.all()

    users = User.objects.all()
    for user in users:
        li = user.addresses.all()
        user.addr_list = li
    return render(request, 'users.html', context={'users': users})
