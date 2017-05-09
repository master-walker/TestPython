#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017��5��9��

@author: Administrator
'''
import time

print time.time()
print time.localtime(time.time())
print time.asctime(time.localtime(time.time()))
print time.ctime(time.time())
print time.mktime((2009, 2, 17, 17, 3, 38, 1, 48, 0))
#格式化时间
print time.strftime("%Y-%m-%d %H:%M:%S")