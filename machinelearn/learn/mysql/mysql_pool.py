import pymysql
from DBUtils.PooledDB import PooledDB
from machinelearn.learn.mysql import DbConfig


class DbPool():

    """
    1. mincached，最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接
    2. maxcached，最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
    3. maxconnections，最大的连接数，
    """
    def __init__(self):
        self.pool = PooledDB(creator = pymysql, host=DbConfig.host, user=DbConfig.user, passwd=DbConfig.passwd,
                               db=DbConfig.db, port=int(DbConfig.port),mincached=2,maxcached=2,maxconnections=2)


    def queryMany(self, name):
        try:
            sql = "select * from t_user where name = %s limit 2"

            # 连接数据池
            coon = self.pool.connection()
            cursor = coon.cursor()
            cursor.execute(sql, name)
            fetchmany = cursor.fetchmany(3)
            print(str(fetchmany))
        except Exception as e:
            print("多笔查询失败，参数：" + str(name), e)

dbpool = DbPool()
dbpool.queryMany("ukar")