# wopapa-example

和媳妇儿一起爬虫小练习

爬虫程序重要的分为两个部分：

- 分析目标组成
- 书写爬虫程序

书写程序：

- 结构清晰

> 可以将其规划为一个爬虫的请求模版

其结构体现为：

```python
# pass 未实现函数
import random

import time


class xxxSpidet(object):
    def __int__(self):
        # 定义初始化变量，比如base url, 计数等变量
        pass

    def get_html(self):
        # 获取响应内容，注意使用随机UA
        pass

    def parse_html(self):
        # 使用正则表达式来解析页面,提取数据
        pass

    def save_html(self):
        # 保存数据， 本地文件、数据库等
        pass

    def run(self):
        # 主函数，用来组合整体逻辑
        pass


if __name__ == '__main__':
    # 程序运行
    spider = xxxSpidet()
    spider.run()
    # 进行1-2秒休眠，防止反爬虫
    time.sleep(random.randint(1, 2))
```