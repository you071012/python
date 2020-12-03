"""
装饰器演练
装饰器：在不修改一个函数的情况下对该函数功能增强
"""


"""
对test方法进行增强打印日志功能，添加log方法，接收参数为一个方法
同一个文件中该方法要放在需要增强的方法上面，否则编译失败

testFunc("a123") 相当于方法不加 @log这么调用 f = log(testFunc)， f("111")

"""
def log(func):
    def wrapper(*args, **kw):
        print('调用方法： %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def testFunc(text):
    print("test方法打印：" + text)




testFunc("a123")
# f = log(testFunc)
# f("111")