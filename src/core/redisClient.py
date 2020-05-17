#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='r-uf61f59b12ebc944.redis.rds.aliyuncs.com', port=6379, password="Chinapnr201")
r = redis.Redis(connection_pool=pool)

# r.set(name = "name", value = "ukar1", ex=10)
key = "CUST_NO_6666000103106145"
val = r.get(key)
if val != None:
    print("redis获取", str(val, encoding="utf-8"))
else:
    print(val)

# delete = r.delete("name")
# print("delete成功", delete)
