# 打开文件 encoding 使用系统默认编码(WIN: GBK, Mac,Linux:UTF-8)
file = open("a.txt", encoding="UTF-8")
# 读写文件（设定读取的字符数量）
content = file.read(8)
print(content)

# 读取一行
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(2)) # 读取一行的n个字节
print(file.readline())

print("***************************")
# 读取多行
lines = file.readlines()
print(lines)
# for line in lines:
#     print(line)

# 关闭文件
file.close()
