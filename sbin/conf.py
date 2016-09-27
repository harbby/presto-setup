#coding:utf-8
# all 公共配置 格式为json
allconf={
"http-server.http.port":16060
,"discovery.uri":"http://master:16060"
,"query.max-memory":"8GB"
,"query.max-memory-per-node":"1GB"
}
## node 配置
#注意: node.id=BROAD-TECH-IDEAL-HP-6666*****  **会被host替换(可以不做修改)
#node.data-dir 会自动配置为安装目录
#一般只需要 修改 node.environment 这两个 node.data-dir即可
node={
"node.environment":"broadtech"
,"node.id":"BROAD-TECH-IDEAL-HP-6666*****"
,"node.data-dir":"********"
}




