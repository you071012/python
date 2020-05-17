# 单独导入Peroson类, Man类
from src.core.class_demo import Person, Man
from src.core import class_demo as clazz

person = clazz.Person("ukar111", "18")
print(person.name)
