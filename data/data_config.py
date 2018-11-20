# -*- coding:utf-8 -*-
from enum import Enum,unique

@unique
class global_var(Enum):
    # case_id
    id = 0
    request_name = 1
    url = 2
    run = 3
    request_method = 4
    header = 5
    case_depend = 6
    data_depend = 7
    field_depend = 8
    data = 9
    expect = 10
    result = 11

# 获取case_id
def get_id():
    return global_var.id.value

# 获取请求名称
def get_request_name():
    return global_var.request_name.value

# 获取url
def get_url():
    return global_var.url.value

# 获取是否run
def get_run():
    return global_var.run.value

# 获取请求方法
def get_request_method():
    return global_var.request_method.value

# 获取是否有请求头
def get_header():
    return global_var.header.value

# 获取依赖用例
def get_case_depend():
    return global_var.case_depend.value

# 获取依赖数据
def get_data_depend():
    return global_var.data_depend.value

# 获取依赖字段
def get_field_depend():
    return global_var.field_depend.value

# 获取请求数据
def get_data():
    return global_var.data.value

# 获取预期结果
def get_expect():
    return global_var.expect.value

# 获取实际结果
def get_result():
    return global_var.result.value



if __name__ == '__main__':
    print(global_var.request_name.value)