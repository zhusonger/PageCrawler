# -*- coding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "pan_zhusong", "123456", "pan_zhusong")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

try:
    sql = "SELECT rid, vid FROM `dzz_resources` WHERE username='xuyi' AND name='urls.txt'"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    result = cursor.fetchone()
    rid = result[0]
    vid = result[1]
    print("rid=%s,vid=%s" % (rid, vid))

    sql = "SELECT skey, sval FROM `dzz_resources_attr` WHERE rid='%s' AND vid='%s' AND skey='aid'" % (rid, vid)
    # 执行SQL语句
    cursor.execute(sql)
    result = cursor.fetchone()
    skey = result[0]
    sval = result[1]
    print("skey=%s,sval=%s" % (skey, sval))

except Exception as e:
    print("Error: unable to fetch data", e)


# 关闭数据库连接
db.close()
