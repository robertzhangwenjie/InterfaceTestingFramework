# -*- coding:utf-8 -*-
import xlrd,os
from xlutils.copy import copy
from data.get_data_config import GetDataConfig

class OperationExcel(object):
    def __init__(self,file_name=None,sheet_id=0):
        if file_name:
            self.file_name = file_name
        else:
            data_config_path = GetDataConfig().CONFIG_PATH
            self.file_name = os.path.join(data_config_path,'interface_cases.xls')
            self.sheet_id = sheet_id

        self.data = self.get_data()

    # 获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(filename=self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)


    # 写入excel
    def write_value(self,row,col,value):
        '''
        写入excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    # 根据对应的case_id 找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        row_values = self.get_row_values(row_num)
        return row_values


    # 根据对应的case_id找到对应的行号
    def get_row_num(self,case_id):
        col_data = self.get_col_values()
        try:
            num = col_data.index(case_id)
        except Exception as e:
            raise ValueError('case_id %s:不存在'%case_id)
        return num

    # 根据行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 根据列号，找到该列的内容，默认找第0列的
    def get_col_values(self,col_id=None):
        if col_id != None:
            col_data = self.data.col_values(col_id)
        else:
            col_data = self.data.col_values(0)
        return col_data






if __name__ == '__main__':
    opers = OperationExcel()
    col_values=opers.get_col_values(0)
    print(col_values)