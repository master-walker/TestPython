#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月10日

@author: Administrator
'''
import os,sys,re,shutil


path="D:\\testProject\\TestFile"
movePath="D:\\testProject"
for fileName in os.listdir(path):
    findMode=re.sub(r"22", "11", fileName)
    if findMode!=fileName:
        newName=os.path.join(path,findMode)
        oldName=os.path.join(path,fileName)
        os.rename(oldName,newName)
        moveFile=os.path.join(movePath,findMode)
        shutil.copyfile(newName,moveFile)
#         print newName  
        
        