#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2018/10/31 6:42
# @Author   :   robert
# @FileName :   get_data_config.py
# @Software :   PyCharm

import os

class GetDataConfig(object):

    def __init__(self):
        self.PROJECT_PATH = self.__get_project_path()
        self.CONFIG_PATH = self.__get_config_path()

    # 获取项目根目录路径
    def __get_project_path(self):
        project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        return project_path


    # 获取配置文件目录路径
    def __get_config_path(self):
        data_config_path = os.path.join(self.PROJECT_PATH, 'data_config')
        return data_config_path

    # 获取邮件配置文件
    def get_email_config(self):
        email_config = os.path.join(self.CONFIG_PATH,'email_config.yaml')
        return email_config



if __name__ == '__main__':
    data_config = GetDataConfig()
    print(data_config.get_email_config())

