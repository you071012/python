#!/usr/bin/env python
# -*- coding:utf8 -*-

# 不包含返回值函数定义
def person(name ,age=20):
    print("name is :" + name.title() + ", age is :" + str(age))

person("ukar", 18)
person("ukar")
person(name="ukar", age=18)
person(age=18, name="ukar")

# 包含返回值函数定义
def get_full_name(frist_name, last_name):
    return frist_name + " " + last_name

print(get_full_name("you", "jia"))

# 可变参数 *表示，会将参数当作元组
def param(frist, *second):
    print(type(second))
    print(second)
param("one", " two", "three")

# 可变参数 **表示，会将参数当作字典。注意传参时，可变参数前面必须加上**
def param2(frist, **second):
    print(type(second))
    print(second)
dict_={"name":"ukar", "age":18}
param2("one", **dict_)

def listTest(arr):
    arr[0]["name"] = "aa"
arrs = [{"name":"ukar"}, {"name":"nihao"}]
listTest(arrs)
print(arrs)