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
try:
    print(1/0)
except BaseException as be:
    print("error....", be)
else:
    print("there is no error")
finally:
    print("finally...")