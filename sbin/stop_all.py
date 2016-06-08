#!/usr/bin/env python2
#coding=utf-8
import os,sys
##  print sys.path[0],'------' ###获取当前文件的所在的绝对路径
pwd=sys.path[0]

##################用于找出 所有的master和slave名称
def listwork(path):
##################用于找出 所有的master和slave名称
	rd=open(path,'r+')
	line=rd.readline().strip()  #读取一行
	tmp=[]
	while line:
		if not ('#' in line or line=='\n'):
			tmp.append(line)
		line=rd.readline().strip()  #读取一行
	rd.close()
	#print tmp
	return  tmp
#######################################

###############
if __name__=='__main__':
	master=listwork(pwd+'/master')
	slaves=listwork(pwd+'/slaves')
	print 'master=',master
	print 'slaves=',slaves
	#### 下面开始 合并 分发文件
	nameall=reduce(lambda x,y:x if y in x else x+[y], [[],]+master+slaves)  ##犀利的去合并重复语句
	print 	nameall
	for i in nameall:
		os.system('ssh '+i+' \''+pwd+'/../bin/launcher stop\'')


