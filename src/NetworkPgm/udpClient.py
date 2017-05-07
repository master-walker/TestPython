#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月4日

@author: Administrator
'''
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


for data in ["test1","test2"]:
    sock.sendto(data,("127.0.0.1",9999))
    print sock.recv(1024)
sock.close()
