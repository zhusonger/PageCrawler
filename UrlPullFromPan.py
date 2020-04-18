# -*- coding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "pan_zhusong", "123456", "pan_zhusong")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "SELECT rid, vid FROM `dzz_resources` WHERE username='xuyi' AND name='urls.txt'"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        rid = row[0]
        vid = row[1]
        # 打印结果
        print("rid=%s,vid=%s" % (rid, vid))
except Exception as e:
    print("Error: unable to fetch data", e)

# 关闭数据库连接
db.close()
