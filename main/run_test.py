# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from base.runmethod import RunMethod
from data.get_data import GetData
from util.common import CommonUtil
from util.send_email import SendEmail
from data.dependent_data import DependentData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
from data.get_config_path import GetDataConfig
import json
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()

    # 程序执行
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                header = self.data.get_header(i)
                expect = self.data.get_expect_data(i)
                id = self.data.get_case_id(i)
                # 获取数据所依赖的字段
                dependent_field = self.data.get_dependent_field(i)
                if dependent_field:
                    dependent_case_id = self.data.get_dependent_case_id(i)
                    self.dependent_data = DependentData(dependent_case_id)
                    # 获取依赖的数据
                    dependent_data = self.dependent_data.get_dependent_data(i)
                    # 将依赖的数据赋予相应的依赖
                    data[dependent_field] = dependent_data
                if header == 'write':
                    res = self.run_method.post_main(url=url,data=data)
                    ops_header = OperationHeader(res)
                    ops_header.wirte_cookie()
                    res = res.json()
                elif header == 'yes':
                    ops_json = OperationJson(GetDataConfig().get_cookie_config())
                    cookie = ops_json.datas
                    res = self.run_method.run_main(method=method,url=url,data=data,cookies=cookie)
                else:
                    res =self.run_method.run_main(method=method,url=url,data=data)

                # res = self.run_method.run_main(method=method,url=url,data=data,header=header)
                res = json.dumps(res,ensure_ascii=False,indent=4,sort_keys=True)
                print(res)
                if self.com_util.is_contain(expect,res):
                    print(f'{id}:测试通过')
                    self.data.write_result(i,'pass')
                    pass_count.append(id)
                else:
                    print(f'{id}:测试失败')
                    self.data.write_result(i, res)
                    fail_count.append(id)
        self.send_email.send_report(pass_count,fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

