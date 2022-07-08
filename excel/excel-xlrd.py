# xlrd模块介绍
# python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库
# 为什么使用xlrd模块？
# 在UI自动化或者接口自动化中数据维护是一个核心，所以此模块非常实用
# 安装
# pip3 install xlrd
# 注意 xlrd 2.0.1 不支持xlxs,所以安装1.2.0版本
# pip3 install xlrd==1.2.0
# 使用介绍
# 常用单元格的数据类型
# empty（空的）
# string（text）
# number
# date
# boolean
# error
# blank（空白表格）
# 导入模块


import xlrd


def excelRow(filename):
    # 打开excel
    data = xlrd.open_workbook(filename)  # 文件名以及路径，如果路径或者文件名有中文给前面加一个 r
    table = data.sheets()[0]
    print(table)
    # table = data.sheet_by_index(sheet_indx)  # 通过索引顺序获取
    # table = data.sheet_by_name(sheet_name)  # 通过名称获取
    # 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
    names = data.sheet_names()  # 返回book中所有工作表的名字
    # data.sheet_loaded(sheet_name or indx)  # 检查某个sheet是否导入完毕
    print(names)
    # 行操作 (行号参数从0开始)
    nrows = table.nrows  # 获取该sheet中的行数，注，这里table.nrows后面不带().
    print(nrows)
    row = table.row(1)  # 返回由该行中所有的单元格对象组成的列表,这与tabel.raw()方法
    print(row)
    row1 = table.row_slice(2)  # 返回由该行中所有的单元格对象组成的列表
    print(row1)
    # 返回由该行中所有单元格的数据类型组成的列表；　　　　
    # 返回值为逻辑值列表，若类型为empy则为0，否则为2
    row2 = table.row_types(3, start_colx=0, end_colx=None)
    print(row2)
    row3 = table.row_values(2, start_colx=0, end_colx=None)  # 返回由该行中所有单元格的数据组成的列表
    print(row3)
    len = table.row_len(2)  # 返回该行的有效单元格长度，即这一行有多少个数据
    print(len)


def excelColnum(filename):
    # 打开excel
    data = xlrd.open_workbook(filename)  # 文件名以及路径，如果路径或者文件名有中文给前面加一个 r
    table = data.sheets()[0]
    ncols = table.ncols  # 获取列表的有效列数
    print(ncols)
    colnum = table.col(1, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表
    print(colnum)
    colnum1 = table.col_slice(2, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表
    print(colnum1)
    colnum2 = table.col_types(0, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据类型组成的列表
    print(colnum2)
    colnum3 = table.col_values(3, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据组成的列表
    print(colnum3)


def excelCell(filename):
    # 打开excel
    data = xlrd.open_workbook(filename)  # 文件名以及路径，如果路径或者文件名有中文给前面加一个 r
    table = data.sheets()[0]
    cell = table.cell(0, 1)  # 返回单元格对象
    print(cell)
    cell1 = table.cell_type(0, 2)  # 返回对应位置单元格中的数据类型
    print(cell1)
    cell2 = table.cell_value(1, 2)  # 返回对应位置单元格中的数据
    print(cell2)


if __name__ == '__main__':
    excelCell("/Users/yz/workspace/center/test.xls")
