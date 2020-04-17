# -*- coding: utf-8 -*-

import time
import LasongEmail
import sys

print(sys.argv)

folder = sys.argv[1] if len(sys.argv) > 0 else "pics_" + time.strftime("%Y_%m_%d", time.localtime())
print(folder)


def read_urls():
    '''读取txt文件，返回一个列表，每个元素都是一个元组;文件的格式是图片保存的名称加英文逗号加网页地址'''
    with open('urls.txt', 'r') as f:
        lines = f.readlines()
    the_urls = []
    for line in lines:
        try:
            the_list = line.strip().split(",")
            if len(the_list) >= 2 and the_list[0] and the_list[1]:
                desc = the_list[2] if len(the_list) > 2 else ""
                the_urls.append((folder + "/" + the_list[0] + ".png", the_list[1], desc))
        except Exception as e:
            print(e)
    return the_urls


def send():
    # 发送邮件
    contents = []
    for the_url in urls:
        contents.append((the_url[2], the_url[0]))

    LasongEmail.send_email("song.zhu@kascend.com", '每日截图-' + time.strftime("%Y-%m-%d", time.localtime()),
                           contents)


# 你输入的参数
urls = read_urls()
send()
