#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月3日

@author: Master SkyWalker2
'''
import socket

#创建socket
sockt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
sockt.connect(("127.0.0.1",3328))

#接收数据
# print sockt.recv(1024)

for data in ["test1","test2"]:
    sockt.send(data)
    print sockt.recv(1024)
    
sockt.send('exit')
sockt.close()