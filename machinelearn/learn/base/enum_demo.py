from enum import Enum,unique

# @unique
class Color(Enum):
    # RED = "1"
    # BLUE = "2"
    # YELLOW = "3"
    # RED_BAK = "1"
    RED = {"name":"red","code":1}
    BLUE = {"name":"blue","code":2}
    RED_BAK = {"name":"red","code":1}

# 打印枚举值和属性
print(Color.RED.name)
print(Color.RED.value)

# 遍历枚举，相同value值的枚举不会遍历出来，会认为是第一个值的副本,如果不想要枚举有重复的值，在枚举类上加注解 @unique,需要导入unique模块
for color in Color:
    print("name is " + color.name + ",value is " + str(color.value))

#遍历出值相同的枚举
for color in Color.__members__.items():
    color_ = color[1]
    print("__members__，name is " + color_.name + ",value is " + str(color_.value))
