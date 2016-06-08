# presto-setup
加快presto部署和启动

master 文件里为coordinator 节点

slaves 文件里面为 工作节点

start_all.py 为集群启动脚本
stop_all.py 为集群关闭脚本

安装：

1，自行创建etc文件夹 
按需创建jvm.config log.properties catalog
而 config.properties和node.properties 安装时会自动创建

2，sbin 目录下相关配置
local.properties 文件里面配置 单机模式   >> config.properties内容
coordinator.properties 里面放 coordinator节点的配置  >> config.properties
worker.properties  里面放 工作节点 的配置 >> config.properties

node.properties文件里面存放 node配置 
注意: node.id=BROAD-TECH-IDEAL-HP-6666*****  **会被host替换(可以不做修改)
一般只需要 修改 node.environment 这两个 node.data-dir即可

配置完成后 执行 下面脚本即可  注意后面是要安装到集群的路径
./setup.py setup-Path
