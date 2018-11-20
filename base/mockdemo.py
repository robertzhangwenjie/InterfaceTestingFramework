# -*- coding:utf-8 -*-

from mock import Mock


# 模拟mock封装
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res