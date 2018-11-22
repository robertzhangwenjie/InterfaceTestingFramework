# -*- coding:utf-8 -*-
import json,os
from data.get_config_path import GetDataConfig


class OperationJson(object):

    def __init__(self,json_filename=None):
        self.json_filename = json_filename
        if self.json_filename is None:
            self.json_filename = os.path.join(GetDataConfig().CONFIG_PATH,'package.json')

        self.datas = self.read_data(self.json_filename)
    # 读取json文件
    def read_data(self,json_filename):
        with open(json_filename) as fp:
            data = json.load(fp)
        return data

    def get_data(self,key):
        if key:
            value = self.datas[key]
        else:
            value = None
        return value

    # 写
    def write_data(self,data):
        cookie_config = GetDataConfig().get_cookie_config()
        with open(cookie_config,'w') as fp:
            fp.write(json.dumps(data))

if __name__ == '__main__':
    opes = OperationJson('../data_config/package.json')
    print(opes.datas)
    print(opes.get_data('name'))
