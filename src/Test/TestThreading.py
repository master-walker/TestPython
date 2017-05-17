#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月11日

@author: Administrator
'''
import time,threading

def printInfo():
    n=0
    while n<5:
        print "currentTime:"+time.ctime(time.time())
        n=n+1
    
def printInfo2():
    n=0
    while n<3:
        print "currentTime2:"+time.ctime(time.time())
        n=n+1   
    
# printInfo()

thread1=threading.Thread(target=printInfo())
thread2=threading.Thread(target=printInfo2())
thread1.start()
thread2.start()
thread1.join()
thread2.join()
