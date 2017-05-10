#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月9日

@author: Administrator
'''
import os
with open("../Test/TestTime.py","r") as f:
    print f.read(100)
    position=f.tell()
    print position
#     position=f.seek(0,0)
    print f.read(50)

# os.rename("D:/testProject/TestFile/TestFile002.pdf","D:/testProject/TestFile/TestName.pdf")
# os.remove("D:/testProject/TestFile/TestFile003.ppt")
# os.mkdir("D:/testProject/TestFile/testDir")
print os.getcwd()
os.rmdir("D:/testProject/TestFile/testDir")

    