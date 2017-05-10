#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月10日

@author: Administrator
'''
import re

str1="this is a re Test string hello 123456 yes"

num=re.compile(r"\d+")
strPatn=re.compile(".+is")
print strPatn.search(str1).group()
matchobj=num.search(str1)
if matchobj:
    print matchobj.string
    print matchobj.re
    print matchobj.group()
    print matchobj.pos
    print matchobj.endpos
    print matchobj.lastindex
    print matchobj.group
    print matchobj.groups
    print matchobj.groupdict
    
    
    
    
    
    
    
    
    