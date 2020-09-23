# !/usr/bin/python
# -*- coding: utf-8 -*-

test_str='hello word'

# 获取字符串长度
len = len(test_str)
print("test_str长度：", str(len))

# 标题化每个英文字段（每个字母首字母大写），如果不是英文，还是原字符串输出
title_str = test_str.title()
print("标题化字符串：", title_str)

# 字符串首字母大写(只会整个字符串将首字母大写)，如果不是英文，还是原字符串输出
capitalize_str = test_str.capitalize()
print("字符串首字母大写：", capitalize_str)

# 字符串填充，当前字符串居中，两个参数，var1：填充后字符串总长度，var2：两边填充字符
center_str = test_str.center(20, '*')
print(center_str)

#按照指定字符去除首尾字符，不传参数代表去空格
strip_str = test_stracct_refersh.py
print("字符传去除首尾空格：" , strip_str)

test_split_str = "hello&world"
split_str = test_split_str.split("&")
print("字符串分割：" , split_str)

# 字符串拼接
print("我是%s，今年%d岁" % ("ukar", 18))

#将指定字符添加到字符串每个字母之间，返回一个新的字符串
str_join = "&".join(test_str)
print(str_join)

# 字符串位置查找（从左往右），返回第一次找到字符串的索引，未找到返回-1，rfind()从右往左找
find = test_str.find("lo")
print("字符串位置查找" ,find)

# 字符串左补0，参数为字符串总长度，若参数小于当前字符串长度返回当前字符串，大于则在左补0至参数长度返回
print("字符串左补0：", test_str.zfill(8))
