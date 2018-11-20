#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2018/10/29 13:42
# @Author   :   robert
# @FileName :   operation_yaml.py
# @Software :   PyCharm

from ruamel import yaml

class OperationYaml(object):

    def __init__(self,yaml_filename):
        self.yaml_filename = yaml_filename
        self.datas = self.read_data(self.yaml_filename)


    # 读取yaml文件
    def read_data(self,yaml_filename):
        with open(yaml_filename,'rb') as f:
            data = yaml.load(f,Loader=yaml.RoundTripLoader)
        return data

    # 根据key获取数据
    def get_data(self,key):
        if key:
            value =  self.datas[key]
            return value
        else:
            return None





if __name__ == '__main__':
    email_config = 'D:\interface_test\data_config\email_config.yaml'
    with open(email_config,'rb') as f:
        content = yaml.load(f,Loader=yaml.RoundTripLoader)

        print(type(content))
        print(content['Email'])

    with open(email_config,'w') as f:
        yaml.dump(content,f,Dumper=yaml.RoundTripDumper)
        print(content)


