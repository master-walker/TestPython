#!/usr/bin/python
#coding=utf-8

'''
Created on 2017年5月4日

@author: Administrator
'''
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(("127.0.0.1",9999))

while True:
    data,addr=sock.recvfrom(1024)
    print "receive from %s:%s" %addr
    sock.sendto("hello %s",data,addr)