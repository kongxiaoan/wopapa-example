# 导包,发起请求使用urllib库的request请求模块
from urllib import request


# 获取百度响应对象
def getBaiduResponse():
    # urlopen()向URL发请求,返回响应对象,注意url必须完整
    response = request.urlopen('http://www.baidu.com/')
    print(response)
    return response


# 输出HTML信息
def getBaiduHtmlContent():
    response = getBaiduResponse()
    html = response.read().decode('utf-8')
    print(html)


def getHttpbin():
    # 向网站发送get请求
    response = request.urlopen('http://httpbin.org/get')
    html = response.read().decode()
    print(html)


#     {
#   "args": {},
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.8",  很明显这里做了反爬虫处理，UA，所以我们需要重构爬虫UA信息
#     "X-Amzn-Trace-Id": "Root=1-626a3e68-1257c1e25598a0a63a32f341"
#   },
#   "origin": "137.59.102.104",
#   "url": "http://httpbin.org/get"
# }

# ============================对比

# {
#   "args": {},
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0", //模拟成了MAC电脑访问
#     "X-Amzn-Trace-Id": "Root=1-626a3f2b-654d31a139b1c68c49018f98"
#   },
#   "origin": "137.59.102.104",
#   "url": "http://httpbin.org/get"
# }

def refactor_get_httpbin():
    # 定义变量：URL 与 headers
    url = 'http://httpbin.org/get'  # 向测试网站发送请求
    # 重构请求头，伪装成 Mac火狐浏览器访问，可以使用上表中任意浏览器的UA信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
    # 1、创建请求对象，包装ua信息
    req = request.Request(url=url, headers=headers)
    # 2、发送请求，获取响应对象
    res = request.urlopen(req)
    # 3、提取响应内容
    html = res.read().decode('utf-8')
    print(html)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # getHttpbin()
    refactor_get_httpbin()
