# !/usr/bin/python
# -*- coding:utf8 -*-

name = 'ukar'
age = 18
if name == 'ukar' and age == 18:
    print("ukar is 18 years old")

if name == 'ukar' or age == 20:
    print("ukar is not 20 years old")

if age < 18:
    print("age less than 18")
elif age > 18:
    print("age more than 18")
else:
    print("age is 18")

_name_list = ["zhangsan", "lisi", "wangwu"]
user_name = 'lisi'
if user_name in _name_list:
    print("%s is in name_list" % user_name)
else:
    print("%s is not in name_list" % user_name)

#判断列表是否为空，在Python中，False,0,'',[],{},()都可以视为假。
_list = []
if _list:
    print("列表为不空")
else:
    print("列表为空")