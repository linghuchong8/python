"""
1. 导入socket模块
2. 创建socket套接字
3. 建立tcp连接（和服务端建立连接）
4. 开始发送数据（到服务端）
5. 关闭套接字
"""
# 1. 导入socket模块
import socket

# 2. 创建socket套接字
# 参数1：family: AddressFamily 地址簇，类型
#       AF_INET:    IPv4
#       AF_INET6:   IPv6
# 参数2：type: SocketKind 协议类型
#       SOCK_STREAM： TCP协议
#       SOCK_DGRAM：  UDP协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. 建立tcp连接（和服务端建立连接）
# 参数元组：("ip", port)服务器的ip和port的元组
tcp_client_socket.connect(("127.0.0.1", 8080))

# 4. 开始发送数据（到服务端）
# 不能直接发字符串，需要进行编码，得到字节数组
tcp_client_socket.send("你好，我是客户端！abc123".encode("utf-8"))
# 使用gbk，会导致网络调试助手乱码
# tcp_client_socket.send("你好，我是客户端！abc123".encode("gbk"))

# 5. 关闭套接字
tcp_client_socket.close()