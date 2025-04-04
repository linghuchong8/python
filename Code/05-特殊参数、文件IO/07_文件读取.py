# 打开文件 encoding 使用系统默认编码(WIN: GBK, Mac,Linux:UTF-8)
file = open("a.txt", encoding="UTF-8" )
# 读写文件
content = file.read()
print(content)
# 关闭文件
file.close()
