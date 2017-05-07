#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017��5��3��

@author: Master SkyWalker2
'''

import socket



sockt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockt.bind(("127.0.0.1",3328))

sockt.listen(5)

sock,addr=sockt.accept()

while True:
    sock.send("welcome")
    data=sock.recv(1024)
    if data=="exit" or not data:
        break
    print 'hello %s' %data
   
sock.close()

print "connect %s:%s closed" %addr