# -*- coding:utf-8 -*-
import pymysql
import time
import configparser



class DtlLogRefersh():
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("./refersh_config.ini")
        trans_rds_key = "Trans-Database"
        param_key = "Param-Config"

        self.host = cf.get(trans_rds_key, "host")
        self.user = cf.get(trans_rds_key, "user")
        self.passwd = cf.get(trans_rds_key, "passwd")
        self.database = cf.get(trans_rds_key, "database")
        self.port = int(cf.get(trans_rds_key, "port"))

        self.trans_date = cf.get(param_key, "trans_date")
        self.max_id = cf.get(param_key, "max_id")
        self.count = 0
    def refersh(self):

        rds_db = pymysql.connect(host=self.host, port=self.port, user=self.user,
                             password=self.passwd,database=self.database)
        rds_cursor = rds_db.cursor()

        # 查询所有产品号
        product_dict = {}
        product_sql = "select system_id, open_acct_rgn from product_info where 1 = 1"
        rds_cursor.execute(product_sql)
        cursor_fetchall = rds_cursor.fetchall()
        for item in cursor_fetchall:
            product_dict[item[0]] = item[1]

        trans_log_sql = "select trans_id from trans_log where trans_date = '%s' and acct_stat = 'W'  and id <= %s"\
                        % (self.trans_date, self.max_id)
        rds_cursor.execute(trans_log_sql)
        transIds = rds_cursor.fetchall()

        print("开始准备执行刷分区，共计%d条trasnLog待处理" % len(transIds))
        trans_id_list = []
        total = 0
        for transId in transIds:
            trans_id_list.append(transId[0])
            if len(trans_id_list) % 200 == 0:
                self.do_update(trans_id_list, product_dict, rds_db, rds_cursor)
                total = total + 200
                trans_id_list = []
                print("当前共执行%d条" % (total))
        if len(trans_id_list) > 0:
            self.do_update(trans_id_list, product_dict, rds_db, rds_cursor)
            total = total + len(trans_id_list)
            print("当前共执行%d条" % (total))
        rds_db.close()

    def do_update(self, trans_id_list, product_dict, rds_db, rds_cursor):
        sql = "select t1.id, t2.biz_product_id from trans_dtl_log t1 inner join acct_info t2 " \
              "on t1.cust_id = t2.cust_id and t1.acct_id = t2.acct_id " \
              "where t1.trans_date = '%s' " % self.trans_date
        sql = sql + " and t1.trans_id in (%s)" % ','.join(['%s'] * len(trans_id_list))
        rds_cursor.execute(sql, trans_id_list)
        upd_list = rds_cursor.fetchall()
        try:
            upd_dict = {}
            # 将upd_list中元素按照产品号归类
            for item in upd_list:
                id = item[0]
                product_id = item[1]
                if (not upd_dict) or (product_id not in upd_dict.keys()):
                    id_list = []
                    id_list.append(id)
                    upd_dict[product_id] = id_list
                else:
                    id_list = upd_dict[product_id]
                    id_list.append(id)
                    upd_dict[product_id] = id_list

            for key, val in upd_dict.items():
                upd_sql = "update trans_dtl_log set acct_rgn_id = '%s' where trans_date = '%s'" % (product_dict[key], self.trans_date)
                upd_sql = upd_sql + " and id in (%s)" % ','.join(['%s'] * len(val))
                rds_cursor.execute(upd_sql, val)
                rds_db.commit()
        except Exception as e:
            print("刷新分区号失败", e)
            rds_db.rollback()

dtlLogRefersh = DtlLogRefersh()
dtlLogRefersh.refersh()