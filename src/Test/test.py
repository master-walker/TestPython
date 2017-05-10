#coding=utf-8


from config.config import config

# cfg=config()
print config.db_host
print config.db_passwd

def testFun():
    str1="hello"
    print locals()
    print globals()
    
testFun()
print locals()
print globals()
    
    