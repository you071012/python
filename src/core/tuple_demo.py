# !/usr/bin/python
# -*- coding:utf8 -*-

####元组操作，元组中值不可被改变
_tuple = ("zhangsan", "lisi", "wangwu")

print("获取元组指定索引值：" , _tuple[0])

#获取元组指定区间值，包头不包尾
print("获取元组指定区间值：" , _tuple[0:-1])

print("获取元组所有值：" , _tuple[0:])

print("name is %s %s %s ok" % _tuple)
