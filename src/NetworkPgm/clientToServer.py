#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月4日

@author: Administrator
'''
import socket


#创建socket对象
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
sock.connect(("www.sina.com.cn",80))
# sock.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')      
sock.send("GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n")     
             
buffer=[]
while True:
    d=sock.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=''.join(buffer)

header,html=data.split('\r\n\r\n',1)

print header

with open("sina.html","wb") as f:
    f.write(html)




