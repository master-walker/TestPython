#!/usr/bin/env python
#coding=utf-8
'''
Created on 2017年5月18日

@author: Administrator
'''
import logging 


#创建logger
logger_name='example'
logger=logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)


#crate file handler
log_path="./log.log"
fh=logging.FileHandler(log_path)
fh.setLevel(logging.WARN)

#crate formatter
fmt="%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt="%a %Y-%m-%d %H:%M:%S"
formtter=logging.Formatter(fmt,datefmt)

#add hander and formatter to logger
fh.setFormatter(formtter)
logger.addHandler(fh)

# print log info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')




