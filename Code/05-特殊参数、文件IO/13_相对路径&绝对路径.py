lst = [
    "我有一个毛衫1",
    "显得很忠诚2", 
    "望庐山瀑布3"
]
lst = [f"{item}\n" for item in lst]

# 打开文件 /正，上坡   \反，下坡
f = open("./c.txt", "a", encoding="utf8")
# f = open("../实战开发01-贪吃蛇/abc.txt", "a", encoding="utf8")
# f = open("D:\\Python\\Lessons\\Code\\05-特殊参数、文件IO\\c.txt", "a", encoding="utf8")
# f = open("D:/Python/Lessons/Code/05-特殊参数、文件IO/c.txt", "a", encoding="utf8")
# 写出内容
f.writelines(lst)
# 关闭文件
f.close()