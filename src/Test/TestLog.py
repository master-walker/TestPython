#!/usr/bin/env python
#coding=utf-8

'''
Created on 2017年5月18日

@author: Administrator
'''


import logging

logging.basicConfig(filename='testlog',level=logging.ERROR)

logging.debug("debug msg")

logging.info("info msg")

logging.warn("warn msg")

logging.error("error msg")

logging.critical("critical msg")