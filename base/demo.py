# -*- coding:utf-8 -*-
import json

import requests


class RunMain(object):


    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)


    def send_post(self,url,data):
        res = requests.post(url,data)
        return res


    def send_get(self,url,data):
        res = requests.get(url=url,params=data)
        return res


    def run_main(self,url,method,data=None):
        res = None
        if method == 'GET' or method == 'get':
            res = self.send_get(url,data)
        else:
            res =  self.send_post(url,data)
        return res

if __name__ == '__main__':
    data = {
        'username': 'robert',
        'passwd': 'eee'

    }
    baseurl = 'http://127.0.0.1:8888/test/'
    run = RunMain()
    print(run.run_main(url=baseurl,method='GET',data=data))
    print()
