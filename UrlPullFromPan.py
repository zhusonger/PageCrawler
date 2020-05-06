# -*- coding: utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "pan_zhusong", "123456", "pan_zhusong")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

try:
    # 查找文件的唯一标志
    sql = "SELECT rid, vid FROM `dzz_resources` WHERE username='xuyi' AND name='urls.txt'"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    result = cursor.fetchone()
    rid = result[0]
    vid = result[1]
    print("rid=%s,vid=%s" % (rid, vid))

    # 查找aid去找缓存文件路径
    sql = "SELECT skey, sval FROM `dzz_resources_attr` WHERE rid='%s' AND vid='%s' AND skey='aid'" % (rid, vid)
    # 执行SQL语句
    cursor.execute(sql)
    result = cursor.fetchone()
    skey = result[0]
    sval = result[1]
    print("skey=%s,sval=%s" % (skey, sval))

    sql = "SELECT aid, filename, attachment FROM `dzz_attachment` WHERE aid='%s'" % sval
    # 执行SQL语句
    cursor.execute(sql)
    result = cursor.fetchone()
    aid = result[0]
    filename = result[1]
    attachment = result[2]
    print("aid=%s,filename=%s, filename=%s" % (aid, filename, attachment))

    pan_path = "/www/wwwroot/pan.lasong.com.cn/data/attachment/" + attachment
    local_path = "urls.txt"
    pan_file = open(pan_path, 'r')
    local_file = open(local_path, 'w')
    # 若文件不存在,报错，若存在，读取
    for line in pan_file:
        print(line)
        local_file.write(line)
    pan_file.close()
    local_file.close()
except Exception as e:
    print("Error: unable to fetch data", e)

# 关闭数据库连接
db.close()
