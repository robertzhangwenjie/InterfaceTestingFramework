#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2018/11/21 6:23
# @Author   :   robert
# @FileName :   operation_header.py
# @Software :   PyCharm

import requests,json
from util.operation_json import OperationJson

class OperationHeader:

    def __init__(self,response):
        self.response = response

    # 获取cookie
    def get_cookie(self):
        cookie = self.response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookie)
        return cookie

    # 写入cookie
    def wirte_cookie(self):
        ops = OperationJson()
        ops.write_data(self.get_cookie())


