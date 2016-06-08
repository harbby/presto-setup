#!/usr/bin/env python2
#coding=utf-8
import os,sys
##  print sys.path[0],'------' ###获取当前文件的所在的绝对路径
pwd=sys.path[0] #当前路径
print sys.argv[1]
setup_path=sys.argv[1]
#setup_path='/ideal/123/presto-server-0.147'     #待安装到的目录
#setup_path='/opt/cloudera/parcels/CDH/lib/presto-server-0.147'     #待安装目录

x=raw_input('即将安装presto到:'+setup_path+'目录下\n 是否继续(y or n)? ')
if x not in ['y','Y']:
    print '取消安装'
#--------------------------------------------------------------------------------------

'''
注意！
本程序从msater 节点开始会分发程序，进行配置 并完成安装
'''
##################用于找出 所有的master和slave名称
def listwork(path):
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
def getnodecf(name):         ###获取node 配置
    outtmp=''
    with open(pwd+'/node.properties','r+') as rd:
        tmp=map(lambda x:x.strip(),rd)
        for i in tmp:
            if 'node.id' in i:
                outtmp+=i.replace('*','')+name.upper()+'\n'
            elif 'node.data-dir' in i:
                outtmp+='node.data-dir='+setup_path+'/data'+'\n'
            else:
                outtmp+=i+'\n'
        rd.close()
    #-----write file
    print outtmp
    return outtmp
	

###############
if __name__=='__main__':
    ##去掉 setup_path 结尾的/ 符号 
    if setup_path[-1]=='/':
        setup_path=setup_path[:-1]
    print setup_path

    ##清理可能存在的垃圾
    os.system('rm -rf '+pwd+'/../data')      ## rm data
    os.system('find '+pwd+'/../ -name *~  -exec rm -f {} \;') 

    print 'find '+pwd+'/../ -name \'*~\' -exec rm -f {} \;'
    os.system('find '+pwd+'/../ -name \'*~\' -exec rm -f {} \;')  ##清理垃圾
    ## 获取节点列表
    master=listwork(pwd+'/master')
    slaves=listwork(pwd+'/slaves')
    print 'master=',master
    print 'slaves=',slaves
    #### 下面开始 合并 分发文件
    nameall=reduce(lambda x,y:x if y in x else x+[y], [[],]+master+slaves)  ##去重复 合并
    print nameall
    scpok=1   ##0 是完成
    for i in nameall:
        print 'next setup '+i+'-----------------------------'
        cmd='scp -r '+pwd+'/../* '+i+':'+setup_path+'/'
        print cmd
        os.system('ssh '+i+'  mkdir -p '+setup_path)      ##创建目录
        scpok=os.system(cmd)      ##发送
        if scpok==0:
            print i,'scp 发送完成'
        else:
            print i,'scp 发送失败!'
    ### 下面开始 config 配置文件安装
    
    for i in nameall:
        if i in slaves:
            if i in master:     ## in master and slaves
                print i,' 是local模式 next setup local!'
                os.system('ssh '+i+'  \'cat '+setup_path+'/sbin/local.properties > '+setup_path+'/etc/config.properties\'')
            else:   ## in slaves
                print i,'setup slave节点'
                os.system('ssh '+i+'  \'cat '+setup_path+'/sbin/worker.properties > '+setup_path+'/etc/config.properties\'')
        else:   ## in master
            print i,'setup master节点'
            os.system('ssh '+i+'  \'cat '+setup_path+'/sbin/coordinator.properties > '+setup_path+'/etc/config.properties\'')
		
        ### 下面进行node 设置
        #print 'ssh '+i+'  \'echo \"'+setnodecf(i)+'\" > '+setup_path+'/etc/node.properties\''
        os.system('ssh '+i+'  \'echo \"'+getnodecf(i)+'\" > '+setup_path+'/etc/node.properties\'')


