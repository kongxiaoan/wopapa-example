# 拼接 url 地址
# 发送请求
# 将照片保存至本地
from urllib import request
from urllib import parse


def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    # 此处使用urlencode()进行编码
    params = parse.urlencode({'wd': word})
    url = url.format(params)
    return url


# 创建请求对象-Request
# 获取响应对象-urlopen
# 获取响应内容-read
def test_request(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    # 请求对象 + 响应对象 + 提取内容
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件至本地
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # getHttpbin()
    word = input('请输入搜索内容：')
    url = get_url(word)
    filename = word + '.html'
    test_request(url, filename)
