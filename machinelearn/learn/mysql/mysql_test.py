# -*- coding:utf-8 -*-
import pymysql
import cryptography
import time

# 打开数据库连接
def init_db():
    db = pymysql.connect(host='localhost', port=3307, user='root', password='071012',database='ukar')
    return db

# 单笔插入
def insertOne(name, age):
    db = init_db()
    cursor = db.cursor()
    sql = "insert into t_user (name, age) values (%s, %s)"
    params = [name, age]
    cursor.execute(sql, params)
    db.commit()
    db.close()

"""
    批量插入
"""
def insertMany(list):
    db = init_db()
    cursor = db.cursor()
    sql = "insert into t_user (name, age) values (%s, %s)"
    try:
        cursor.executemany(sql, list)
        db.commit()
        # print("批量插入成功，参数：" + str(list))
    except:
        print("批量插入失败，参数：" + str(list))
        db.rollback()
    finally:
        db.close()

def queryOne(id ,name):
    db = init_db()
    cursor = db.cursor()
    sql = "select * from t_user where id = %s and name like %s"

    try:
        params = [id, name] # params = (id, name) 使用元组也可以，但是不建议
        cursor.execute(sql, params)
        fetchone = cursor.fetchone()
        print(str(fetchone))
    except Exception as e:
        print("单笔查询失败，参数：" + str(id))
    finally:
        db.close()

def queryMany(name):
    db = init_db()
    cursor = db.cursor()
    sql = "select * from t_user where name = %s"

    try:
        cursor.execute(sql, name)
        fetchmany = cursor.fetchmany(3)
        print(str(fetchmany))
    except Exception as e:
        print("多笔查询失败，参数：" + str(name), e)
    finally:
        db.close()

def queryIn(ids, name):
    db = init_db()
    cursor = db.cursor()
    sql = "select * from t_user where id in (%s)" % ','.join(['%s'] * len(ids))
    sql = sql + " and name like %s"

    params = ids
    params.append(name)
    try:
        cursor.execute(sql, params)
        fetchall = cursor.fetchall()
        print(fetchall)
    except Exception as e:
        print("in查询失败", e)
    finally:
        db.close()

# 参数传递建议用列表，而不是使用元组

# insertOne('ukarAAA', 18)
# insertMany([('ukar', 19),('ukar', 20)])
# queryOne(1, 'ukar%')
# queryMany("ukar1")
# queryIn([1,2], 'ukar%')