# !/usr/bin/python
# -*- coding:utf8 -*-

"""
导入模块，会按照sys.path路径逐级查找,使用as 可以定义别名 eg：from src.core import function_demo as fu
使用*可以导入模块中所有函数 eg：from src.core.function_demo import * 不建议使用
"""
# from machinelearn.learn.base import function_demo
# from machinelearn.learn.base.function_demo import get_full_name
# import sys
import functools
# function_demo.person("aa", 11)
# print(get_full_name("zhang", " san"))
# print(sys.path)


# 闭包 函数中返回函数
def createCounter(num):
    def counter():
        return 1 + num
    return counter
f = createCounter(3)
print(f())

# 偏函数functools.partial 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# int() 将指定数字转化为10进制，base参数表示当前传入的数字的进制数
int2 = functools.partial(int, base=16)
print(int2("f"))