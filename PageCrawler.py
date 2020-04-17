# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import LasongEmail

folder = "pics_" + time.strftime("%Y_%m_%d", time.localtime())
if not os.path.exists(folder):
    os.makedirs(folder)


def get_image(local_url, pic_name):
    # 控制浏览器写入并转到链接
    driver.get(local_url)
    time.sleep(1)
    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(local_url, width, height)
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    time.sleep(1)
    # 截图并关掉浏览器
    driver.save_screenshot(pic_name)


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


# 设置chrome开启的模式，headless就是无界面模式
# 一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_experimental_option('mobileEmulation', {'deviceName': 'Galaxy S5'})
driver = webdriver.Chrome(options=chrome_options)
# 你输入的参数
urls = read_urls()
for url in urls:
    get_image(url[1], url[0])
driver.close()
send()
