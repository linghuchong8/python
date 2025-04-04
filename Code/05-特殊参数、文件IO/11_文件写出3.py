lst = [
    "append",
    "低头思故乡", 
    "望庐山瀑布"
]
lst = [f"{item}\n" for item in lst]

# 打开文件 
f = open("c.txt", "a", encoding="utf8")
# 写出内容
f.writelines(lst)
# 关闭文件
f.close()