lst = [
    "append",
    "低头思故乡", 
    "望庐山瀑布"
]
lst = [f"{item}\n" for item in lst]


# 使用with打开文件(管道，网络，蓝牙，串口) ，会在内容结束后，自动关闭
with open("c.txt", "a", encoding="utf8") as f:
    # 写出内容
    f.writelines(lst)
    a = 1 / 0
    
print("关闭文件:", f.closed)