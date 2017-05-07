#coding=utf-8
'''
Created on 2017年5月4日

@author: Administrator
'''

from sqlalchemy import String,Column,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
Base=declarative_base()
class User(Base):
    
    #表名
    __tablename__="user"
    #表结构
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    
    