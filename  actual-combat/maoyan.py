# https://www.maoyan.com/films?showType=1
# https://www.maoyan.com/films?showType=1&offset=0
# https://www.maoyan.com/films?showType=1&offset=30
# https://www.maoyan.com/films?sortId=2
# https://www.maoyan.com/board/7?timeStamp=1651202849344&channelId=40011&index=4&signKey=b9f9535b0a240ad5fb6f2181c8681200&sVersion=1&webdriver=false
import string
# from urllib import request
import requests
import re
import time
import random
import csv
from ua_info import ua_list


# <div class="channel-detail movie-item-title" title="我是真的讨厌异地恋">
#       <a href="/films/1328765" target="_blank" data-act="movies-click" data-val="{movieId:1328765}">我是真的讨厌异地恋</a>
#     </div>

# <div class="channel-detail movie-item-title">.*?title="(.*?)">
# 定义一个爬虫类
class MaoyanSpider(object):
    # 初始化
    # 定义初始页面url
    def __init__(self):
        self.url = 'https://www.maoyan.com/films?showType=1&offset={}'

    # 请求函数
    def get_html(self, url):
        req = requests.get(url=url, headers={'User-Agent': random.choice(ua_list)})
        req.encoding = 'utf-8'
        html = req.text
        print(html)
        # 直接调用解析函数
        self.parse_html(html)

    # 解析函数
    def parse_html(self, html):
        # 正则表达式
        re_bds = '<div class="channel-detail movie-item-title".*?title="(.*?)">'
        # 生成正则表达式对象
        pattern = re.compile(re_bds, re.S)
        # r_list: [('我不是药神','徐峥,周一围,王传君','2018-07-05'),...] 列表元组
        r_list = pattern.findall(html)
        print(r_list)
        self.save_html(r_list)

    # 保存数据函数，使用python内置csv模块
    def save_html(self, r_list):
        # 生成文件对象
        with open('maoyan.csv', 'a', newline='', encoding="utf-8") as f:
            # 生成csv操作对象
            writer = csv.writer(f)
            # 整理数据
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                # 上映时间：2018-07-05
                # 切片截取时间
                time = r[2].strip()[5:15]
                L = [name, star, time]
                # 写入csv文件
                writer.writerow(L)
                print(name, time, star)

    # 主函数
    def run(self):
        # 抓取第一页数据
        for offset in range(0, 31, 30):
            url = self.url.format(offset)
            print(url)
            self.get_html(url)
            # 生成1-2之间的浮点数
            time.sleep(random.uniform(1, 2))


# 以脚本方式启动
if __name__ == '__main__':
    # 捕捉异常错误
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("错误:", e)
