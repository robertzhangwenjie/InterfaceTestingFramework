# -*- coding:utf-8 -*-
import json
import os
import unittest

import sys

from base.demo import RunMain
from mock import Mock
from HtmlTestRunner import HTMLTestRunner
from base.mockdemo import mock_test

class TestMethod(unittest.TestCase):
    #
    # @classmethod
    # def setUpClass(cls):
    #     print('class method')
    #
    # @classmethod
    # def tearDownClass(cls):
    #      print('class teardown')

    def setUp(self):
        self.run = RunMain()

    # def tearDown(self):
    #     print('end...')

    def test_01(self):
        data = {
            'username': 'robert',
            'passwd': 'eee'

        }
        url = 'http://127.0.0.1:8888/test/'

        # self.run.run_main = Mock(return_value=data)
        res = mock_test(self.run.run_main,data,url,'GET',data)
        # res = self.run.run_main(url=url,method='GET',data=data)
        # print(json.dumps(res.json(),indent=2,sort_keys=True))
        # self.passwd = res.json()['passwd']
        self.passwd = res['passwd']
        globals()['passwd'] = self.passwd
    # 跳过测试，原因为"test_02"
    # @unittest.skip('test_02')
    def test_02(self):
        print(passwd)
        print('test02')



if __name__ == '__main__':
    project_path = os.path.abspath(__file__)
    project_path = os.path.dirname(os.path.dirname(project_path))
    # print(project_path)
    report_path = os.path.join(project_path,'report')
    # fp = open(file_path,'wb')
    suite = unittest.TestSuite()
    # tests=[TestMethod('test_01'),TestMethod('test_02')]
    # suite.addTests(tests)
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))

    # print(suite.countTestCases())
    runner = HTMLTestRunner(output=report_path,report_title="this ia first")
    runner.run(suite)
    # fp.close()