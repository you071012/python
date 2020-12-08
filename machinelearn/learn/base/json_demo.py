import json

dict_data={"name":"zhangsan","age":18}
str_data="this is a str"

# 序列化为json串
print(json.dumps(dict_data))
print(json.dumps(str_data))

# json串反序列化
loads = json.loads(json.dumps(dict_data))
print(loads)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
    }

class Stu(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

# 复杂对象json序列化，default需要指定给一个序列化方法 等同于  json.dumps(s, default=student2dict)
s = Stu("ukar",18)
print(json.dumps(s, default=lambda s : s.__dict__))