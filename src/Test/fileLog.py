# -*- encoding:utf-8 -*-
import logging
import logging.config
from config.logger import getLogger
# class test(object):
#     logging.config.fileConfig("../config/logging_conf.ini")
#     def __init__(self):
#         # create logger
#         logger_name = "example"
#         self.logger = logging.getLogger(logger_name) 
#     def testlog(self):
#         try:
#             a=1/0
#         except Exception as e:
#             
#             logger=self.logger
#             logger.debug(e)
#             logger.info('info message')
#             logger.warn('warn message')
#             logger.error('error message')
#             logger.critical('critical message')
#         
# if __name__=="__main__":
#     test=test()
#     test.testlog()
logger=getLogger()
logger.debug("e")
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')