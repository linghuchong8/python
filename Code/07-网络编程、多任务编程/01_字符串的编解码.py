# 把字符串str数据转成字节数组bytes （默认用utf-8编码）
bytes_arr = "你好abc123我有一个帽衫".encode(encoding="utf-8")
print(bytes_arr, type(bytes_arr))
# aaa = b'\xe4\xbd\xa0\xe5\xa5\xbdabc123'
# 把bytes字节数组转成字符串
string = bytes_arr.decode(encoding="utf-8")
print(string)

# 把字符串str数据转成字节数组bytes （默认用utf-8编码）
bytes_arr = "你好".encode(encoding="utf-8")
print(bytes_arr, type(bytes_arr))
# 把bytes字节数组转成字符串
string = bytes_arr.decode(encoding="gbk")
print(string)

# 把字符串str数据转成字节数组bytes （默认用utf-8编码）
bytes_arr = "你好".encode(encoding="gbk")
print(bytes_arr, type(bytes_arr))
# 把bytes字节数组转成字符串
string = bytes_arr.decode(encoding="utf-8")
print(string)