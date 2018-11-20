#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2018/10/19 6:10
# @Author   :   robert
# @FileName :   common.py
# @Software :   PyCharm

from util.operation_excel import OperationExcel

class CommonUtil(object):

    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否再另外一个字符串中
        :param str_one: 查找的字符串
        :param str_two: 被查找的字符串
        :return: True or False
        '''
        flag = None
        try:
            if str_one is None:
                raise TypeError('预期结果为空！')
        except TypeError:
            return False
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

if __name__ == '__main__':
    str_one = '"loginName": "13995553697"'
    str_two='''{
    "code": 1,
    "data": {
        "createTime": "2018-09-06 14:38:57",
        "customerId": "1527683372619",
        "customerName": "武汉诚迈科技有限公司",
        "customerUserId": "53f5b7b00a904703a074b1a5bfbfd56b",
        "dataStatus": 1,
        "disable": 0,
        "lateLoginTime": "2018-10-22 08:38:54",
        "loginName": "13995553697",
        "parkId": "af98a32c9b4d490297cadc2d85faf797",
        "parkName": "创意天地",
        "phone": "13995553697",
        "token": "02294ee2061045dda4bb49d6cd5bcb0b",
        "userIcon": "http://oyroeq9vl.bkt.clouddn.com/sys_tb_customer_user/user_icon/97406637dca64ab68478dcb9599b45ca_1_424.jpg",
        "userType": 2
    }
}'''
    comm = CommonUtil()
    print(comm.is_contain(str_one,str_two))