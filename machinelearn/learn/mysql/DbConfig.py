import configparser

cf = configparser.ConfigParser()
cf.read("../../../config/config.ini")  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块

secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，

config_key = "Mysql-Database"
options = cf.options(config_key)  # 获取某个section名为Mysql-Database所对应的键

host = cf.get(config_key, "host")  # 获取[Mysql-Database]中host对应的值
user = cf.get(config_key, "user")  # 获取[Mysql-Database]中host对应的值
passwd = cf.get(config_key, "passwd")  # 获取[Mysql-Database]中host对应的值
db = cf.get(config_key, "db")  # 获取[Mysql-Database]中host对应的值
port = cf.get(config_key, "port")  # 获取[Mysql-Database]中host对应的值

