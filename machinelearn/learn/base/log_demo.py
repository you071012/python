import logging

"""
详细情况需要再学习
"""

logging.basicConfig(level=logging.INFO)

def foo(num):
    logging.info("接口传入参数：%s，%s", str(num), "num")
    try:
        a = num/0
    except BaseException as be:
        logging.error(be)

foo(1)
