# 当 URL 路径或者查询参数中，带有中文或者特殊字符的时候，就需要对 URL 进行编码（采用十六进制编码格式）。URL 编码的原则是使用安全字符去表示那些不安全的字符。
# (安全字符，指的是没有特殊用途或者特殊意义的字符。)

# http://www.biancheng.net/index?param=10 路径和查询字符串之间使用问号?隔开
# 冒号：用于分隔协议和主机组件，斜杠用于分隔主机和路径
# ?：用于分隔路径和查询参数等。
# =用于表示查询参数中的键值对。
# &符号用于分隔查询多个键值对。

# URL 之所以需要编码，是因为 URL 中的某些字符会引起歧义，比如 URL
# 查询参数中包含了”&”或者”%”就会造成服务器解析错误；再比如，URL 的编码格式采用的是 ASCII 码而非 Unicode 格式，
# 这表明 URL 中不允许包含任何非 ASCII 字符（比如中文），否则就会造成 URL 解析错误。

# URL 编码协议规定（RFC3986 协议）：URL 中只允许使用 ASCII 字符集可以显示的字符，比如英文字母、
# 数字、和- _ . ~ ! *这 6 个特殊字符。当在 URL 中使用不属于 ASCII 字符集的字符时，就要使用特殊的符号对该字符进行编码，比如空格需要用%20来表示。

from urllib import parse


def test_url_encode():
    query_string = {
        'wd': '爬虫'
    }
    # 调用parse模块的urlencode()进行编码
    result = parse.urlencode(query_string)
    # 使用format函数格式化字符串，拼接url地址
    url = 'http://www.baidu.com/s?{}'.format(result)
    print(url)


def test_quote():
    # 注意url的书写格式，和 urlencode存在不同
    url = 'http://www.baidu.com/s?wd={}'
    word = input('请输入要搜索的内容:')
    # quote()只能对字符串进行编码
    query_string = parse.quote(word)
    print(url.format(query_string))


# quote() 只能对字符串编码，而 urlencode() 可以直接对查询字符串字典进行编码。因此在定义 URL 时，需要注意两者之间的差异
# # urllib.parse
# urllib.parse.urlencode({'key':'value'}) #字典
# urllib.parse.quote(string) #字符串


def test_unquote():
    string = '%E7%88%AC%E8%99%AB'
    result = parse.unquote(string)
    print(result)


def string_plus_type():
    # 1、字符串相加
    baseurl = 'http://www.baidu.com/s?'
    params = 'wd=%E7%88%AC%E8%99%AB'
    url = baseurl + params
    # 2、字符串格式化（占位符）
    params = 'wd=%E7%88%AC%E8%99%AB'
    url = 'http://www.baidu.com/s?%s' % params
    # 3、format()方法
    url = 'http://www.baidu.com/s?{}'
    params = 'wd=%E7%88%AC%E8%99%AB'
    url = url.format(params)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # getHttpbin()
    # test_url_encode()
    # test_quote()
    test_unquote()
