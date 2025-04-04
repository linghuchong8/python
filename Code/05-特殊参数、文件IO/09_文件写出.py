# 打开文件 
f = open("b.txt", "w", encoding="utf8")
# 写出内容
f.write("床前明月光, abc123\n")
f.write("垂死病中惊坐起，resposibility\n")
# 关闭文件
f.close()