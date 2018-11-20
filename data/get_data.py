# -*- coding:utf-8 -*-

from util.operation_excel import OperationExcel
from data  import data_config
from util.operation_json import OperationJson

class GetData(object):
    def __init__(self):
        self.operation_excel = OperationExcel()

    # 获取excel行数，就是我们case的个数
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # 获取用例ID
    def get_case_id(self,row):
        col = data_config.get_id()
        case_id = self.operation_excel.get_cell_value(row,col)
        return case_id

    # 获取是否执行
    def get_is_run(self,row):
        col = data_config.get_run()
        run_model = self.operation_excel.get_cell_value(row,col)
        if run_model == 'yes' or run_model == 'YES':
           flag = True
        else:
            return False
        return flag

    # 获取header
    def get_header(self, row):
        col = data_config.get_header()
        header = self.operation_excel.get_cell_value(row,col)
        if header == '':
            return None
        else:
            return header

    # 获取请求方式
    def get_request_method(self,row):
        col = data_config.get_request_method()
        request_method = self.operation_excel.get_cell_value(row,col)
        return request_method

    # 获取url
    def get_request_url(self,row):
        col = int(data_config.get_url())
        url = self.operation_excel.get_cell_value(row,col)
        return url

    # 获取请求数据
    def get_request_data(self,row):
        col = data_config.get_data()
        data = self.operation_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self,row):
        col = data_config.get_expect()
        expect_data = self.operation_excel.get_cell_value(row,col)
        if expect_data == '':
            return None
        return expect_data

    # 将执行结果写入excel
    def write_result(self,row,value):
        col = data_config.get_result()
        self.operation_excel.write_value(row,col,value)

    # 获取依赖用例case_id
    def get_dependent_case_id(self,row):
        col = data_config.get_case_depend()
        dependent_case_id = self.operation_excel.get_cell_value(row,col)
        if dependent_case_id == '':
            return None
        return dependent_case_id


    # 获取依赖数据的key
    def get_dependent_key(self,row):
        col = data_config.get_data_depend()
        dependent_key = self.operation_excel.get_cell_value(row,col)
        if dependent_key == '':
            return None
        return dependent_key

    # 获取需要依赖的字段
    def get_dependent_field(self,row):
        col = data_config.get_field_depend()
        dependent_field = self.operation_excel.get_cell_value(row,col)
        return dependent_field


