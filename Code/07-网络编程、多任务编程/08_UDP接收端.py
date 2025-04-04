"""
UDP接收数据
1. 导入模块socket
2. 创建socket套接字
3. 绑定端口号（必选）
4. 接收数据
5. 关闭套接字
"""
# 1. 导入模块socket
import socket
from utils import decode_data

# 2. 创建socket套接字
# 参数1： 地址类型 
#           AF_INET     IPv4
#           AF_INET6    IPv6
# 参数2：协议类型
#           SOCK_STREAM    TCP
#           SOCK_DGRAM     UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3. 绑定IP&端口（可选）
udp_socket.bind(("", 8888))

print("----------等待接收数据----------")
# 4. 接收数据
# 返回：元组
#   元素1：字节数组类型的数据
#   元素2：发送者IP和端口号的元组
data, addr = udp_socket.recvfrom(2048)

msg = decode_data(data)
print("收到来自【{}】的消息：{}".format(addr, msg))

# data = "你好，陌生人！".encode("UTF-8")
# addr = ("192.168.36.88", 8888) # address
# udp_socket.sendto(data, addr)

# 5. 关闭套接字
udp_socket.close()