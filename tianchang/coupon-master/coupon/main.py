# -- coding:UTF-8 --

import requests
import datetime

# 抢券的时间
scheduled_time = "2019-11-13 13:39"
# 券的URL
requestUrls = ["https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%223KyrVmpGvsiQevJ6qhB1U26gXeh9%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3DBC82F8A182BB1680FB716E88BE8AEC01C2B9929DAE0DF52E8A656B69752C41BB0221EAD203D3B18D858B9D425DDF603A_babel%2CroleId%3D785D22509ADAECFF5EB69C0303537611_babel%22%2C%22eid%22%3A%222COBKBP5GC6TCE3USTVD2U2SPIQJA5XOUMBWDHKHREXERM7ZQOBGIS2CH5YIGN3SM6VRSLDXFZDIC5UEEJY55RBAYE%22%2C%22fp%22%3A%2275b447e7bf072ad1bb6c2513d2acfff0%22%2C%22pageClick%22%3A%22Babel_Coupon%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22%22%2C%22lat%22%3A%22%22%7D%7D&screen=750*1334&client=wh5&clientVersion=1.0.0&sid=&uuid=&area=&loginType=3&callback=jsonp5"]
# 券的Referer
referers = ["https://pro.jd.com/mall/active/3KyrVmpGvsiQevJ6qhB1U26gXeh9/index.html?nsukey=pvo%2BYv2V844KRk183lgqNl6CRJjgXI9EYjsm%2B%2F6cyWxfhv0w4bKTtIzwUNUtb%2FusadYjMJUAt%2Bw%2BMRS44VADgriKNPLScNirDMMEgtd8s%2FVusk%2B0e%2BhTxEPxBhP6VZNUP55WCfWHedjdykYvG9ejHxcJYYwGTpGZpIKsPe5y6YhCc7DiZPeyBU1KGktfSJa0Z%2BCffNhGy4bQCvQp1QuFRg%3D%3D"]
# 浏览器及版本
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'


# 将cookie转为字典
def get_cookie():
    with open("cookie.txt") as f:
        cookies = {}
        for line in f.read().split(';'):
            name, value = line.strip().split('=', 1)
            cookies[name] = value
        return cookies


# 配置Session的参数
session = requests.Session()
session.headers['User-Agent'] = user_agent
session.cookies = requests.utils.cookiejar_from_dict(get_cookie())


# 开始抢券
def getCoupon():
    print('等待抢券中......')
    while (True):
        # 当前时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        # 如果到预定时间就开始发送请求，然后打印结果
        # if now == scheduled_time:
        for i in range(len(requestUrls)):
            session.headers['Referer'] = referers[i]
            response = session.get(requestUrls[i])
            # response.encoding = 'utf-8'
            print(response.text)
        break


if __name__ == '__main__':
    getCoupon()
