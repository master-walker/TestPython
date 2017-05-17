  #!/usr/bin/env python
#coding=utf8
'''
Created on 2017年5月4日

@author: Master SkyWalker2
'''
import MySQLdb,traceback
from config.config import config


def connectDB():
    host=config.db_host
    port=int(config.db_port)
    user=config.db_user
    passwd=config.db_passwd
    dbName=config.db_name
    charset=config.db_charset
    try:
        #创建数据库连接
        conn=MySQLdb.connect(host=host,port=port,user=user,passwd=passwd,db=dbName,charset=charset)
        #创建游标操作数据库
        cursor=conn.cursor()
        
        return cursor
    except Exception:
        print traceback.print_exc()


def selectDB(sql):
    try:
        #创建游标操作数据库
        cursor=connectDB()
        
        #执行Sql
        cursor.execute(sql)
        
        
        
        #获取结果
        return cursor.fetchall()
    
    except Exception:
        print traceback.print_exc()
        

   
if __name__=="__main__":
    print selectDB("select * from persons")
    cursor=connectDB()
    cursor.execute("select version()")
    data=cursor.fetchall()
    print data
    