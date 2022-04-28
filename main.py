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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # getHttpbin()
    getBaiduHtmlContent()
