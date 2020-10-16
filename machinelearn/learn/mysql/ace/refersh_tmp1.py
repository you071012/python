# -*- coding:utf-8 -*-
import pymysql
import sys
import configparser
import time
import datetime
from datetime import datetime as dt


class RefershTmp1():
    def __init__(self):
        argv = sys.argv
        if len(argv) < 3:
            raise AttributeError("请传入分区参数")

        self.acct_date = str(argv[1])
        self.tag = str(argv[2])
        self.last_acct_date = (dt.strptime(self.acct_date, "%Y%m%d").date() + datetime.timedelta(days=-1)).strftime(
            "%Y%m%d")

        self.port = 3306
        cf = configparser.ConfigParser()

        cf.read("./dbconfig.ini")
        if self.tag == "01":
            params_key = "PARAMS-01"
        elif self.tag == "03":
            params_key = "PARAMS-03"
        elif self.tag == "04":
            params_key = "PARAMS-04"
        elif self.tag == "05":
            params_key = "PARAMS-05"
        elif self.tag == "06":
            params_key = "PARAMS-06"
        else:
            raise AttributeError("参数传递错误")

        self.host = cf.get(params_key, "host")
        self.user = cf.get(params_key, "user")
        self.passwd = cf.get(params_key, "passwd")
        self.database = cf.get(params_key, "database")
        print("参数信息，分区：%s，账务日期：%s，昨日账务日期：%s" % (self.tag, self.acct_date, self.last_acct_date))

    def refersh(self):
        startTime = int(str(time.strftime("%Y%m%d%H%M%S", time.localtime())))
        rds_db = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                 password=self.passwd, database=self.database)
        rds_cursor = rds_db.cursor()
        qry_sql = "select acct_no from acct_info where acct_date_tmp2 in ('%s','%s') and acct_date_tmp1 < acct_date_tmp2" % (
        self.last_acct_date, self.acct_date)
        rds_cursor.execute(qry_sql)
        acctNos = rds_cursor.fetchall()
        if (not acctNos):
            print("分区%s没有待刷新数据" % self.tag)
            return
        print("分区%s待更新条数：%d" % (self.tag, len(acctNos)))
        self.do_update(acctNos, rds_db, rds_cursor)
        rds_db.close()
        endTime = int(str(time.strftime("%Y%m%d%H%M%S", time.localtime())))
        print("执行结束时间，耗时：" + str(endTime - startTime) + "秒")

    def do_update(self, acctNos, rds_db, rds_cursor):
        base_sql = "update ACCT_INFO set ACCT_BAL_TMP1 = ACCT_BAL, AVL_BAL_TMP1 = AVL_BAL, FRZ_BAL_TMP1 = FRZ_BAL, ACCT_DATE_TMP1 = ACCT_DATE_TMP2 "

        total = 0
        list = []
        try:
            for i in range(len(acctNos)):
                list.append(acctNos[i])
                total = total + 1
                if (len(list) % 100 == 0):
                    sql = base_sql + "where acct_no in (%s) " % ','.join(['%s'] * len(list))
                    rds_cursor.execute(sql, list)
                    rds_db.commit()
                    list = []
                    print("当前100条更新完毕，共刷新%d条" % total)

            if list:
                sql = base_sql + "where acct_no in (%s) " % ','.join(['%s'] * len(list))
                rds_cursor.execute(sql, list)
                rds_db.commit()
            print("分区%s刷新条数：%d" % (self.tag, total))
        except Exception as e:
            print("出现异常", e)
            rds_db.rollback()


refershTmp1 = RefershTmp1()
refershTmp1.refersh()