# 正则解析

import re

html = """
<div><p>www.biancheng.net</p></div>
<div><p>编程帮</p></div>
<div><p>编程帮1</p></div>
"""
# .	匹配除换行符以外的任意字符
# \w	匹配所有普通字符(数字、字母或下划线)
# \s	匹配任意的空白符
# \d	匹配数字
# \n	匹配一个换行符
# \t	匹配一个制表符
# \b	匹配一个单词的结尾
# ^	匹配字符串的开始位置
# $	匹配字符串的结尾位置
# \W	匹配非字母或数字或下划线
# \D	匹配非数字
# \S	匹配非空白符
# a|b	匹配字符 a 或字符 b
# ()	正则表达式分组所用符号，匹配括号内的表达式，表示一个组。
# [...]	匹配字符组中的字符
# [^...]	匹配除了字符组中字符的所有字符


# *	重复零次或者更多次
# +	重复一次或者更多次
# ？	重复0次或者一次
# {n}	重复n次
# {n,}	重复n次或者更多次
# {n,m}	重复n到m次


# [0123456789]	8	True	在一个字符组里枚举所有字符，字符组里的任意一个字符
# 和"待匹配字符"相同都视为可以匹配。
# [0123456789]	a	False	由于字符组中没有 "a" 字符，所以不能匹配。
# [0-9]	7	True	也可以用-表示范围，[0-9] 就和 [0123456789] 是一个意思。
# [a-z]	s	True	同样的如果要匹配所有的小写字母，直接用 [a-z] 就可以表示。
# [A-Z]	B	True	[A-Z] 就表示所有的大写字母。
# [0-9a-fA-F]	e	True	可以匹配数字，大小写形式的 a～f，用来验证十六进制字符。


# 正则表达式默认为贪婪匹配，也就是尽可能多的向后匹配字符，比如 {n,m} 表示匹配前面的内容出现 n 到 m 次（n 小于 m），在贪婪模式下，首先以匹配 m 次为目标，而在非贪婪模式是尽可能少的向后匹配内容，也就是说匹配 n 次即可。
# 贪婪模式转换为非贪婪模式的方法很简单，在元字符后添加“?”即可实现

# *	*? （左贪婪，右非贪婪）
# +	+？
# ？	??
# {n,m}	{n,m}？

# 需要转义的字符
# * + ? ^ $ [] () {} | \

# re 的方法看源文件

# \w+ 表示匹配多个所有普通字符(数字、字母或下划线)
def test_re():
    # 贪婪匹配，re.S可以匹配换行符
    # 创建正则表达式对象
    pattern = re.compile('<div><p>.*</p></div>', re.S)
    # 匹配HTMLX元素，提取信息
    re_list = pattern.findall(html)
    print(re_list)
    # 非贪婪模式匹配，re.S可以匹配换行符
    pattern = re.compile('<div><p>.*?</p></div>', re.S)
    re_list = pattern.findall(html)
    print(re_list)


def test_patten():
    # 正则表达式分组
    website = "编程帮 www.biancheng.net.1234"
    # 提取所有信息
    # 注意此时正则表达式的 "." 需要转义因此使用 \.
    pattern_1 = re.compile('\w+\s+\w+\.\w+\.\w+\.\w*')
    print(pattern_1.findall(website))

    # 提取匹配信息的第一项
    pattern_2 = re.compile('(\w+)\s+\w+\.\w+\.\w+')
    print(pattern_2.findall(website))

    # 有两个及以上的()则以元组形式显示
    pattern_3 = re.compile('(\w+)\s+(\w+\.\w+\.\w+)')
    print(pattern_3.findall(website))


def test_html_re():
    html = """
    <div class="movie-item-info">
    <p class="name">
    <a title="你好，李焕英">你好，李焕英</a>
    </p>
    <p class="star">
    主演：贾玲,张小斐,沈腾
    </p>    
    </div>
    <div class="movie-item-info">
    <p class="name">
    <a title="刺杀，小说家">刺杀，小说家</a>
    </p>
    <p class="star">
    主演：雷佳音,杨幂,董子健,于和伟
    </p>    
    </div> 
    """
    # 寻找HTML规律，书写正则表达式，使用正则表达式分组提取信息
    # 正则前加r 表示原生字符串
    pattern = re.compile(r'<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>', re.S)
    r_list = pattern.findall(html)
    print(r_list)
    # 整理数据格式并输出
    if r_list:
        for r_info in r_list:
            print("影片名称：", r_info[0])
            print("影片主演：", r_info[1].strip())
            print(20 * "*")


if __name__ == '__main__':
    test_patten()
    test_html_re()
    test_re()