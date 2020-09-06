# !/usr/bin/python
# -*- coding:utf8 -*-
_dict = {"name":"ukar", "age":18}
print(_dict)

# 获取字典中值
print(_dict["name"])

# 字典中增加key-value
_dict["high"] = 175
print(_dict)

# 字典中key对应的value修改
_dict["high"] = 180
print(_dict)

# 删除字典中key-value，永久删除
del _dict["high"]
print(_dict)

# 字典的遍历
for key, val in _dict.items():
    print(key, val)
for key in _dict.keys():
    pass
for val in _dict.values():
    pass
