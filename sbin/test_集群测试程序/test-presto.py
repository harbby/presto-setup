#!/usr/bin/env python2
#coding=utf-8
import os,sys

def test_presto():

    cmd=sys.path[0]+'/../presto-cli --server localhost:16060 --catalog hive -f '+sys.path[0]+'/presto.sql'
    msg=''.join(os.popen(cmd))    

    if '*hive schemas*' in msg:
        print 'presto　启动正常　基本信息如下:'
        print msg
        return 1
    else:
        print msg
        print 'presto　启动配置异常　无法查看hive库信息　无法访问hive数据'
        return 0

if __name__=='__main__':
    test_presto()
