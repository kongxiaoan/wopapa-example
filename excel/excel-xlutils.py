import xlutils
import xlrd
from xlutils.copy import copy


# 3.3.2 拷贝源文件
def fun3_3_2():
    workbook = xlrd.open_workbook('/Users/yz/workspace/center/test.xls')  # 打开工作簿
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_workbook.save("new_test.xls")  # 保存工作簿


# 3.3.3 xlutils读取 写入 Excel 表格信息
def fun3_3_3():
    # file_path：文件路径，包含文件的全名称
    # formatting_info=True：保留Excel的原格式（使用与xlsx文件）
    workbook = xlrd.open_workbook('/Users/yz/workspace/center/test.xls')
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    # 读取表格信息
    sheet = workbook.sheet_by_index(0)
    col2 = sheet.col_values(1)  # 取出第二列
    cel_value = sheet.cell_value(1, 1)
    print(col2)
    print(cel_value)
    # 写入表格信息
    write_save = new_workbook.get_sheet(0)
    write_save.write(0, 0, "xlutils写入！")
    new_workbook.save("new_test1.xls")  # 保存工作簿


if __name__ == '__main__':
    fun3_3_3()
