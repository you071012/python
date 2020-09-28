# -*- coding:utf-8 -*-
import pymysql
import configparser
import sys



class DtlLogRefersh():
    def __init__(self):
        argv = sys.argv
        if len(argv) < 2:
            raise AttributeError("请传入入金分区参数")

        self.tag = argv[1].upper()

        cf = configparser.ConfigParser()
        cf.read("./refersh_config.ini")

        if self.tag == "X":
            params_key = "PARAMS-X"
        elif self.tag == "Y":
            params_key = "PARAMS-Y"
        elif self.tag == "Z":
            params_key = "PARAMS-Z"
        else:
            raise AttributeError("参数传递错误")

        self.host = cf.get(params_key, "host")
        self.user = cf.get(params_key, "user")
        self.passwd = cf.get(params_key, "passwd")
        self.database = cf.get(params_key, "database")
        self.port = int(cf.get(params_key, "port"))

        self.trans_date = cf.get(params_key, "trans_date")
        self.max_id = cf.get(params_key, "max_id")
        self.total = 0
        print("参数信息，分区：%s，日期：%s" %(self.tag, self.trans_date))

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

        trans_log_sql = "select trans_id from trans_log where trans_date = '%s' and trans_stat = 'W'  and trans_type = '1113' and id <= %s"\
                        % (self.trans_date, self.max_id)
        rds_cursor.execute(trans_log_sql)
        transIds = rds_cursor.fetchall()
        print("开始准备执行刷分区，共计%d条trasnLog待处理" % len(transIds))
        trans_id_list = []
        for transId in transIds:
            trans_id_list.append(transId[0])
            if len(trans_id_list) % 200 == 0:
                self.do_update(trans_id_list, product_dict, rds_db, rds_cursor)
                trans_id_list = []
        if len(trans_id_list) > 0:
            self.do_update(trans_id_list, product_dict, rds_db, rds_cursor)

        print("transDtlLog分区%s刷库完成，共计：%d条" % (self.tag,self.total))
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
                self.total = self.total + 1
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
            print("当前一批执行完毕，目前共执行transDtlLog：%d条" % self.total)
        except Exception as e:
            print("刷新分区号失败", e)
            rds_db.rollback()

dtlLogRefersh = DtlLogRefersh()
dtlLogRefersh.refersh()