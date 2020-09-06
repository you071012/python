import pymysql
from DBUtils.PooledDB import PooledDB
from machinelearn.learn.mysql import DbConfig

"""
    感觉下来连接池获取连接和每次创建连接时间基本一致
"""
class MysqlPool(object):
    def __init__(self):
        self.__pool = PooledDB(creator = pymysql, host=DbConfig.host, user=DbConfig.user, passwd=DbConfig.passwd,
                               db=DbConfig.db, port=int(DbConfig.port))

    def get_coon(self):
        return self.__pool.connection()



def queryMany(name):
    try:
        sql = "select * from t_user where name = %s"

        # 连接数据池
        coon = MysqlPool().get_coon()
        cursor = coon.cursor()
        cursor.execute(sql, name)
        fetchmany = cursor.fetchmany(2)
        print(str(fetchmany))
    except Exception as e:
        print("多笔查询失败，参数：" + str(name), e)
    finally:
        cursor.close()

def insertMany(list):

    sql = "insert into t_user (name, age) values (%s, %s)"
    try:
        coon = MysqlPool().get_coon()
        cursor = coon.cursor()
        cursor.executemany(sql, list)
        coon.commit()
        print("批量插入成功，参数：" + str(list))
    except:
        print("批量插入失败，参数：" + str(list))
        coon.rollback()
    finally:
        coon.close()