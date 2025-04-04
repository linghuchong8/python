"""
UDP发送数据
1. 导入模块socket
2. 创建socket套接字
3. 绑定IP&端口（可选）
4. 发送数据
5. 关闭套接字
"""
# 1. 导入模块socket
import socket

# 2. 创建socket套接字
# 参数1： 地址类型 
#           AF_INET     IPv4
#           AF_INET6    IPv6
# 参数2：协议类型
#           SOCK_STREAM    TCP
#           SOCK_DGRAM     UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. 绑定IP&端口（可选）
udp_socket.bind(("", 3333))

# 4. 发送数据sendto
data = "你好，陌生人！".encode("UTF-8")
addr = ("192.168.36.88", 8888) # address
udp_socket.sendto(data, addr)

# 5. 关闭套接字
udp_socket.close()