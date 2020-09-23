# -*- coding:utf-8 -*-
import pymysql
import time

def init_rdsdb():
    db = pymysql.connect(host='rm-uf658580z4h70ymzi.mysql.rds.aliyuncs.com', port=3306, user='poseidon_dev',
                         password='Cpnqc0BLfPxAJKzt',database='poseidon_dev')
    return db

def init_polardb():
    db = pymysql.connect(host='rm-uf658580z4h70ymzi.mysql.rds.aliyuncs.com', port=3306, user='poseidon_dev',
                         password='Cpnqc0BLfPxAJKzt',database='poseidon_dev')
    return db


def refersh():
    print("执行开始时间：" + time.strftime("%Y%m%d%H%M%S", time.localtime()))
    rds_db = init_rdsdb()
    rds_cursor = rds_db.cursor()

    polar_db = init_polardb()
    polar_cursor = polar_db.cursor()

    productIds = ["FSBF"]
    startId = "0"
    sql = "select id,cust_id,acct_id from acct_info where biz_product_id in (%s)" % ','.join(['%s'] * len(productIds))
    sql = sql + " and id > %s order by id asc limit 10"

    total = 0
    try:
        while True:
            params = productIds[:]
            params.append(startId)
            polar_cursor.execute(sql, params)
            fetchmany = polar_cursor.fetchall()
            if not fetchmany:
                print("执行结束，共执行%d条" % total)
                break

            for i in range(len(fetchmany)):
                upd_sql = "update acct_info set acct_rgn_id = '02' where cust_id = %s and acct_id = %s"
                upd_params = fetchmany[i][1:]
                rds_cursor.execute(upd_sql, upd_params)
            rds_db.commit()
            startId = str(fetchmany[len(fetchmany) - 1][0])
            total = total + len(fetchmany)
            print("当前一批刷新完成，共执行%d条" % total)
    except Exception as e:
        print("查询用户信息失败", e)
    finally:
        rds_db.close()
        polar_db.close()
        print("执行结束时间：" + time.strftime("%Y%m%d%H%M%S", time.localtime()))


refersh()