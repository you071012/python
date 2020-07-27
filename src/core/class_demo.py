class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self, food):
        print(self.name + "吃了" + food)

class Work():
    def __init__(self, work="工作"):
        self.work = work


person = Person(name="ukar", age=18)
# print(person.name)
person.eat("苹果")

class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        # 设置sex初始值
        self.sex = "男"
        self.work = Work()

    # 重写父类方法
    def eat(self, food):
        print(self.name + "重写父类方法吃了" + food)

man = Man("aaa",20)
print(man.sex)
man.eat("香蕉")
print(man.work.work)

