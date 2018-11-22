#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2018/10/31 6:36
# @Author   :   robert
# @FileName :   get_email_data.py
# @Software :   PyCharm

from util import operation_yaml
from data.get_config_path import GetDataConfig

class GetEmailData(object):
    def __init__(self,email_config=None):
        self.email_config = email_config
        if self.email_config is None:
            self.email_config = GetDataConfig().get_email_config()
        self.opera_yaml = operation_yaml.OperationYaml(self.email_config)
        self.datas = self.opera_yaml.get_data('Email')
    # 获取接收人地址列表
    def get_to_recivers(self):
        to_recivers = self.datas['to_recivers']
        return to_recivers

    # 获取抄送方地址列表
    def get_cc_recivers(self):
        cc_recivers = self.datas['cc_recivers']
        return cc_recivers

    # 获取暗送方地址列表
    def get_bcc_recivers(self):
        bcc_recivers = self.datas['bcc_recivers']
        return bcc_recivers

    # 获取所有收件人信息
    def get_recivers_list(self):
        recivers = {}
        recivers['to_recivers'] = self.datas['to_recivers']
        recivers['cc_recivers'] = self.datas['cc_recivers']
        recivers['bcc_recivers'] = self.datas['bcc_recivers']
        return recivers

    # 获取服务器相关信息
    def get_server_data(self,server_name='QQ'):
        '''
        获取服务器的信息
        :param server_name: 服务器的名称，默认为QQ服务器，可以选择163，126等
        :return: dict server_data
        '''
        server_data = self.datas['Server'][server_name]
        return server_data


if __name__ == '__main__':
    server_config = {}
    email_data = GetEmailData()
    data = email_data.get_server_data()
    print(email_data.get_recivers_list())












