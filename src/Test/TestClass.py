#!/usr/bin/env python
#coding=UTF-8
'''
Created on 2017年5月10日

@author: Master SkyWalker
'''


class Test(object):
    
    num=0
    
    def __init__(self,name):
        self.name=name
     
    def test1(self):
        global num
        num1=3
        num=num1+1   
        print num
        
        
if __name__=="__main__":
    Test("2").test1()
    print Test("1").num