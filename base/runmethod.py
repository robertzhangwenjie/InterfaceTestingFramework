# -*- coding:utf-8 -*-
# @Time     :   2018/10/19 6:06
# @Author   :   robert
# @FileName :   runmethod.py
# @Software :   PyCharm
import json

import requests

class RunMethod(object):
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,params=data,headers=header)
        else:
            res = requests.get(url=url,params=data)
        return res.json()

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post' or method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=4)
        return res