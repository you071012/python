# -*- coding:utf-8 -*-
import pymysql
import cryptography

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3307, user='root', password='071012',database='ukar')

# 单笔插入
def insertOne(name, age):
    cursor = db.cursor()
    sql = "insert into t_user (name, age) values (%s, %s)"
    params = (name, age)
    cursor.execute(sql, params)
    db.commit()
    db.close()

"""
    批量插入
"""
def insertMany(list):
    cursor = db.cursor()
    sql = "insert into t_user (name, age) values (%s, %s)"
    try:
        cursor.executemany(sql, list)
        db.commit()
        print("批量插入成功，参数：" + str(list))
    except:
        print("批量插入失败，参数：" + str(list))
        db.rollback()
    finally:
        db.close()

def queryOne(id):
    cursor = db.cursor()
    sql = "select * from t_user where id = %s"

    try:
        cursor.execute(sql, id)
        fetchone = cursor.fetchone()
        print(str(fetchone))
    except Exception as e:
        print("单笔查询失败，参数：" + str(id))
    finally:
        db.close()

def queryMany(name):
    cursor = db.cursor()
    sql = "select * from t_user where name = %s"

    try:
        cursor.execute(sql, name)
        fetchmany = cursor.fetchmany(3)
        print(str(fetchmany))
    except Exception as e:
        print("多笔查询失败，参数：" + str(name))
    finally:
        db.close()

# insertOne('ukar', 18)
# insertMany([('ukar', 19),('ukar', 20)])
# queryOne(1)
queryMany("ukar")