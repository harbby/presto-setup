#coding:utf-8
#当前路径(配置文件所在绝对路径) 为pwd变量
pwd=__import__('sys').path[0]
#JAVA_HOME=pwd+'/../jre' #内置jre时　可这样配置路径:相对当前文件的路径

#set JAVA8 HOME (必须配置)
JAVA_HOME='/ideal/hadoop/jdk'

# all 公共配置 格式为json (按需配置)
allconf='''
http-server.http.port=16060
discovery.uri=http://master:16060
query.max-memory=8GB
query.max-memory-per-node=1GB
'''

## node 配置(无需手动修改)
#注意: node.id=BROAD-TECH-IDEAL-HP-6666*****  **会被host替换(可以不做修改)
#node.data-dir 会自动配置为安装目录
#一般只需要 修改 node.environment 这两个 node.data-dir即可
node='''
node.environment=broadtech
node.id=BROAD-TECH-IDEAL-HP-6666*****
node.data-dir=********
'''

##jvm 参数设置(按需修改Xmx大小)
jvm_config='''
-server
-Xmx10G
-XX:+UseConcMarkSweepGC
-XX:+ExplicitGCInvokesConcurrent
-XX:+CMSClassUnloadingEnabled
-XX:+AggressiveOpts
-XX:+HeapDumpOnOutOfMemoryError
-XX:OnOutOfMemoryError=kill -9 %p
-XX:ReservedCodeCacheSize=150M
'''

##　日志级别(无需修改)
log_properties='com.facebook.presto=WARN'


