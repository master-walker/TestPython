#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月8日

@author: Administrator
'''

arr=[1,2,3,4,5,6,7]
arr1=[x for x in range(10)]
print arr1
#删除元素；
del arr[-1]
print arr
#比较两个列表
print cmp(arr1,arr)
#返回最大值
print max(arr)
#扩展列表
arr.extend(arr1)
print arr
#获取匹配值的索引
print arr.index(3)
#插入元素
arr.insert(-1,"test")
print arr
#排序
arr.sort()
print arr










