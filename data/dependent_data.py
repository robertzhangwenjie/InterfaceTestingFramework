#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2018/10/23 8:33
# @Author   :   robert
# @FileName :   dependent_data.py
# @Software :   PyCharm
import json

from jsonpath_rw import parse,jsonpath

from util import operation_excel
from base.runmethod import RunMethod
from data.get_data import GetData
class DependentData(object):

    def __init__(self,case_id,file_name=None,sheet_id=0):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.case_id = case_id
        self.opera_excel = operation_excel.OperationExcel(self.file_name,self.sheet_id)
        self.data = GetData()
    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent_case(self):
        run_method = RunMethod()
        row = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row)
        url = self.data.get_request_url(row)
        method = self.data.get_request_method(row)
        header = self.data.get_header(row)
        res = run_method.run_main(method,url,request_data,header)
        return res

    # 根据依赖的key从执行依赖测试case的响应数据中获取依赖的数据
    def get_dependent_data(self, row):
        dependent_data = self.data.get_dependent_key(row)
        res_data = self.run_dependent_case()
        jsonpath_expr = parse(dependent_data)
        return [match.value for match in jsonpath_expr.find(res_data)][0]


