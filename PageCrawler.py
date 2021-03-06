# -*- coding: utf-8 -*-

import time

from PIL import Image

import LasongEmail
import sys
import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))

local_time = time.localtime()
folder = "screenshot_" + str(local_time.tm_year) + "/"


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
                f_path = folder + the_list[0] + ".jpeg"  # os.path.join(script_dir, )
                the_urls.append((f_path, the_list[1], desc))
                im = Image.open(f_path)
                (x, y) = im.size
                x_s = 720  # define standard width
                y_s = int(y * x_s * 1.0 / x + 0.5)  # calc height based on standard width
                print(x, y, x_s, y_s)
                out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
                out.save(f_path, quality=100)
        except Exception as e:
            print(e)
    return the_urls


def send():
    # 发送邮件
    contents = []
    for the_url in urls:
        f_path = the_url[0]
        contents.append((the_url[2], f_path))

    LasongEmail.send_email(None, '每日截图-' + time.strftime("%Y-%m-%d", time.localtime()),
                           contents)


# 你输入的参数
print(folder)
urls = read_urls()
send()

