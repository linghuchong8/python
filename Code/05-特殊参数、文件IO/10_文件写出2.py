lst = [
    "床前明月光", "疑是地上霜", "举头望明月", "abcdefg"   
]
lst = [f"{item}\n" for item in lst]

# 打开文件 
f = open("b.txt", "w", encoding="utf8")
# 写出内容
f.writelines(lst)
# 关闭文件
f.close()