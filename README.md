# presto-setup
#一键完成 presto部署自动部署和配置，一键部署集群 和 一键启停集群

使用步骤：
将sbin文件夹放到 preto根目录下，然后上传到服务器　master节点任意目录(非安装目录,这里默认master打通了所有的ssh)

sbin目录内容如下：
master 文件里为coordinator 节点
slaves 文件里面为 工作节点

start_all.py 为集群启动脚本
stop_all.py 为集群关闭脚本

安装：
1，按需配置好 以下文件:
conf.py
jvm.config
master 和　slaves文件
2，
配置完成后 执行 下面脚本即可  注意后面是要安装到集群的路径
./setup.py setup-Path
