#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月18日

@author: Administrator
'''

import logging
from logging.config import fileConfig

def getLogger():
    fileConfig("../config/logConf.ini")
    logger=logging.getLogger("example")   
    return logger