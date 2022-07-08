# cvs 数据保存
# https://docs.python.org/zh-cn/3.9/library/csv.html#csv-fmt-params 可参考csv 文件读写
import csv
from random import random

path = 'example/'


def test_single_line_csv():
    # 操作文件对象时，需要添加newline参数逐行写入，否则会出现空行现象
    with open(path + 'eggs.csv', 'w', newline='') as csvfile:
        # delimiter 指定分隔符，默认为逗号，这里指定为空格
        # quotechar 表示引用符
        # writerow 单行写入，列表格式传入数据
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|')
        spamwriter.writerow(['www.biancheng.net'] * 5 + ['how are you'])
        spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])


def test_multiple_lines_csv():
    with open(path + 'eggs1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # 注意传入数据的格式为列表元组格式
        writer.writerows([('hello', 'world'), ('I', 'love', 'you')])


# DictWriter 类以字典的形式读写数据
def test_dictwriter_csv():
    with open(path + 'names.csv', 'w', newline='') as csvfile:
        # 构建字段名称，也就是key
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # 写入字段名，当做表头
        writer.writeheader()
        # 多行写入
        writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Lovely', 'last_name': 'Spam'}])
        # 单行写入
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


# =======================================================================

def test_read_csv():
    with open(path + "eggs.csv", 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def test_read_dictwriter_csv():
    with open(path + 'names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])


if __name__ == '__main__':
    # test_dictwriter_csv()
    test_read_dictwriter_csv()
