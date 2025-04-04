"""
1. 导入模块socket
2. 创建socket套接字
3. 设置允许发送广播
4. 发送广播数据(注意广播地址)
5. 关闭套接字
"""
# 1. 导入模块socket
import socket

# 2. 创建socket套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. 设置允许发送广播
# level:    当前设置的影响范围，SOL_SOCKET只对当前socket生效
# optname:  要设置的属性名： SO_BROADCAST 启用广播
# value:    要设置的属性值：True启用 False禁用
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

# 4. 发送广播数据(注意广播地址)
data = "来村东头老王家吃喜酒!".encode("UTF-8")
addr = ("192.168.36.255", 8888)
udp_socket.sendto(data, addr)

# 5. 关闭套接字
udp_socket.close()
