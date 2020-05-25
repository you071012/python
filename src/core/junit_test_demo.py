import unittest

# from src.core import test_class_demo

class Calc():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;


    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y


"""
    测试类必须继承 unittest.TestCase 类
"""
class TestJunit(unittest.TestCase):
    """
        运行测试之前执行的方法
    """
    def setUp(self) -> None:
        print("开始准备初始化calc类......")
        self.calc = Calc(10, 5)

    """
        运行测试之后执行的方法
    """
    def tearDown(self) -> None:
        print("test运行完毕......")
        pass

    """
        测试方法必须以test开头，否则认为是普通方法
    """
    def add(self):
        add = self.calc.add()
        self.assertEqual(add, 15)

    def test_sub(self):
        sub = self.calc.sub()
        self.assertEqual(sub, 5)

    def test_add(self):
        self.add()

if __name__ == '__main__':
    unittest.main()
