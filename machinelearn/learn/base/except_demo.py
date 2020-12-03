"""
python异常捕获规则
try:
    do soming...
except Exception:
    do soming...
except BaseException:
    do soming...
else:
    do soming...
finaly:
    do soming...
"""
def foo(i):
    try:
        if i == 1:
            # 如果 raise后面什么都不带表示抛出当前异常
            raise BaseException("i 不能等于1")
        print(1 / i)

    except BaseException as be:
        print("error....", be)
    else:
        print("there is no error")
    finally:
        print("finally...")

foo(2)
