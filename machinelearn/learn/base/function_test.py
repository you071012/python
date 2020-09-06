# !/usr/bin/python
# -*- coding:utf8 -*-

"""
导入模块，会按照sys.path路径逐级查找,使用as 可以定义别名 eg：from src.core import function_demo as fu
使用*可以导入模块中所有函数 eg：from src.core.function_demo import * 不建议使用
"""
from machinelearn.learn.base import function_demo
from machinelearn.learn.base.function_demo import get_full_name
import sys
function_demo.person("aa", 11)
print(get_full_name("zhang", " san"))
print(sys.path)
