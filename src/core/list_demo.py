# !/usr/bin/python
# -*- coding:utf8 -*-

########列表是可变的，不可变的列表为元组
_list = ["D","B","C","A"]

#遍历列表
for item in _list:
    print(item, end=",")
print("\r")

#创建数值列表 range()第三个参数可选，表示间隔
list_num = list(range(1,10,3))
print("创建数值列表：", list_num)

#创建列表
list_create = [value.center(3,"_") for value in _list]
print("创建列表：", list_create)

#获取指定索引值
print("获取指定索引值：", _list[0])

#获取指定索引区间值,包头不包尾
print("获取指定索引区间值：", _list[0:2])

#获取指定索到结尾值
print("获取指定索到结尾值：", _list[1:])

#获取开头到指定位置值
print("获取开头到指定位置值：", _list[:3])

#获取列表尾部值，列表为空则报错
print("获取列表尾部值：", _list[-1])

#复制列表
print("复制列表：", _list[:])

#列表追加元素
_list.append("E")
print("列表追加元素：", _list)