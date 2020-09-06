import json

dict_data={"name":"zhangsan","age":18}
str_data="this is a str"

# 序列化为json串
print(json.dumps(dict_data))
print(json.dumps(str_data))

# json串反序列化
loads = json.loads(json.dumps(dict_data))
print(type(loads))