#coding = utf-8
import sys,os
import unittest
sys.path.append("\test_case")
# sys.path.insert(0,'\test_case')
from test_case import youdao1,baidu1

#用例列表
def caselist():
    alltestcasenames = [baidu1.Baidu,youdao1.Youdao]
    return alltestcasenames