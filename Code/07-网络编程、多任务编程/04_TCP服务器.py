"""
TCP服务器
1. socket创建一个套接字
2. bind绑定ip和port
3. listen使套接字设置为被动模式
4. accept等待客户端的链接
5. recv/send接收发送数据
"""
# 0. 导入socket模块
from socket import socket, AF_INET, SOCK_STREAM
# 1. socket创建一个套接字
tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 2. bind绑定ip和port, 如果ip是空字符串, 代表绑定所有网卡的8888端口
tcp_server_socket.bind(("", 8888))

# 3. listen使套接字设置为被动模式
# 参数：客户端链接队列的最大个数，只在windows下生效
tcp_server_socket.listen(128)
# 此时，socket套接字对象由主动连接模式变为被动模式，只能等待客户端接入

print("-------------------服务器已开启，等待客户端接入---------------------")
# 4. accept等待客户端的链接(阻塞当前线程，有新的客户端接入，自动释放阻塞)
# 服务器会为每一个连进来的客户端，创建一个socket对象，以后和该客户端的数据收发都是通过这个socket
tcp_client, tcp_client_addr = tcp_server_socket.accept()
print("有新的客户端接入：", tcp_client_addr)

# 5. recv/send接收发送数据(没收到会一直阻塞)
client_data = tcp_client.recv(2048)
print("收到来自【{}】的数据：{}".format(tcp_client_addr, client_data.decode("GBK")))

# 服务器回复客户端消息
tcp_client.send("消息已收到".encode("utf-8"))
tcp_client.close()

# 6. tcp关闭套接字
tcp_server_socket.close()