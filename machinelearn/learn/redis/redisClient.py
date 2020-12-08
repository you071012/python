#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='r-uf6ku5jsrzr1h5hfxo.redis.rds.aliyuncs.com', port=6379, password="Chinapnr201")
# pool = redis.ConnectionPool(host='localhost', port=6379, password="")
r = redis.Redis(connection_pool=pool)

# r.set(name = "name", value = "ukar1", ex=10)
key = "ACCT_NO_6666000103262803_B00423216"
# val = r.get(key)
# if val != None:
#     print("redis获取", str(val, encoding="utf-8"))
# else:
#     print("redis获取值不存在")


def delete():
    keys = r.keys("ACCT_NO_*")
    if not keys:
        for key in keys:
            r.delete(key)
# delete = r.delete("name")
# print("delete成功", delete)
