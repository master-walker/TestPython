#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月4日

@author: Master SkyWalker
'''
import ConfigParser
import os,sys

src_path=os.path.abspath("..")
sys.path.append(src_path)
reload(sys)

class config(object):
    
    def __init__(self,path="..\config\config.ini"):
        
        config=ConfigParser.ConfigParser()
        config.read(path)
        #mysql数据库
        self.db_host=config.get("mskdb","db_host")
        self.db_port=config.get("mskdb","db_port")
        self.db_user=config.get("mskdb","db_user")
        self.db_passwd=config.get("mskdb","db_passwd")
        self.db_name=config.get("mskdb","db_name")
        self.db_charset=config.get("mskdb","db_charset")
        
        
if __name__!="__main__":
    config=config()
        